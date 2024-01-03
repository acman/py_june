from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from categories.models import MainCategory


def category_list(request: HttpRequest) -> HttpResponse:
    objects = MainCategory.objects.prefetch_related("category_set").all()

    return render(request, "categories/category_list.html", {"objects": objects})
