from django.db.models import Count, Q, Case, When, Value, IntegerField
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from categories.models import Category, MainCategory
from posts.models import Post


def category_list(request: HttpRequest) -> HttpResponse:
    objects = MainCategory.objects.prefetch_related(
        "categories", "categories__posts", "categories__posts__comments").all()

    return render(request, "categories/category_list.html",
                  {"objects": objects})


def category_detail(request: HttpRequest, category_slug: str) -> HttpResponse:
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category_id=category.id, is_active=True)
    paginator = Paginator(posts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "categories/category_detail.html",
        {"page_obj": page_obj, "category": category},
    )
