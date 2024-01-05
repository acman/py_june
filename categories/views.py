from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from categories.models import Category, MainCategory
from posts.models import Post


def category_list(request: HttpRequest) -> HttpResponse:
    objects = MainCategory.objects.prefetch_related("category_set").all()

    return render(request, "categories/category_list.html", {"objects": objects})


def category_detail(request: HttpRequest, category_id: int) -> HttpResponse:
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category_id=category.id, is_active=True)

    return render(
        request,
        "categories/category_detail.html",
        {"posts": posts, "category": category},
    )
