from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from posts.models import Post

from .forms import CommentForm


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
            comment.save()
            return redirect("categories:detail", category_slug=post.category.slug)

        return render(request, self.template_name, {"form": form, "post": post})
