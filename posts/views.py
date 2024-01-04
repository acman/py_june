from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from categories.models import Category
from posts.forms import PostForm
from posts.models import Post



class CreatePostView(LoginRequiredMixin, View):
    template_name = "posts/post_form.html"
    login_url = "/users/login/"

    def get(self, request: HttpRequest, category_id: int) -> HttpResponse:
        category = Category.objects.get(pk=category_id)
        form = PostForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest, category_id: int) -> HttpResponse:
        form = PostForm(request.POST)
        category = Category.objects.get(pk=category_id)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.category = category
            post.save()
            return redirect("categories:list")

        return render(request, self.template_name, {"form": form, "category": category})


class DetailsPostView(View):
    template_name = "posts/post_detail.html"
    template_name_2 = "posts/post_unavailable.html"

    def get(self, request: HttpRequest, post_id: int) -> HttpResponse:
        post = Post.objects.get(pk=post_id)
        context = "This post is currently unavailable"

        if post.is_active:
            return render(request, self.template_name, {"post": post})

        return render(request, self.template_name_2, {"context": context})
