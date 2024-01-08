from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from posts.models import Post

from .forms import CommentForm
from .models import Comment


class CreateCommentView(LoginRequiredMixin, View):
    template_name = "comments/comment_form.html"
    login_url = "/users/login/"

    def get(self, request: HttpRequest, post_slug: str) -> HttpResponse:
        post = get_object_or_404(Post, slug=post_slug)
        form = CommentForm()
        return render(request, self.template_name, {"form": form, "post": post})

    def post(self, request: HttpRequest, post_slug: str) -> HttpResponse:
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=post_slug)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = self.request.user
            comment.post_id = post.pk
            comment.save()
            return redirect("categories:detail", category_slug=post.category.slug)

        return render(request, self.template_name, {"form": form, "post": post})

# Тут пробую створити редагування коменту, за аналогією до посту. Не розумію як тепер потрапити на цю сторінку
# оскільки за таким url /comments/update/title-2-3/ видає помилку Generic detail view UpdateCommentView
# must be called with either an object pk or a slug in the URLconf. Не можу зрозуміти як правильно побудувати url
# і аналогічно для revers_lazy, в нас комент підвязаний до посту. Можливо цей базовий вью не дає зробити те що хочу
class UpdateCommentView(UserPassesTestMixin, UpdateView):
    model = Comment
    slug_url_kwarg = "comment_slug"
    fields = ["title", "content"]
    template_name = "comments/comment_update.html"
    success_url = reverse_lazy("categories:list")

    def test_func(self):
        return self.get_object().author == self.request.user

