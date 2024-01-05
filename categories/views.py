from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from categories.models import Category, MainCategory
from posts.models import Post


def category_list(request: HttpRequest) -> HttpResponse:
    objects = MainCategory.objects.prefetch_related("category_set").all()

    return render(request, "categories/category_list.html", {"objects": objects})


def category_detail(request: HttpRequest, category_id: int) -> HttpResponse:
    objects = Post.objects.filter(category_id=category_id, is_active=1)
    category = Category.objects.filter(pk=category_id)

    return render(
        request,
        "categories/category_detail.html",
        {"objects": objects, "category": category},
    )
