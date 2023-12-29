from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from categories.models import Category
from posts.decorator import user_required
from posts.forms import PostForm


@method_decorator(user_required, name="dispatch")
class CreatePostView(View):
    template_name = 'posts/post_form.html'

    def get(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        form = PostForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, category_id):
        form = PostForm(request.POST)
        category = Category.objects.get(pk=category_id)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.category = category
            post.save()
            return redirect("categories:list")

        return render(request, self.template_name, {"form": form, "category": category})