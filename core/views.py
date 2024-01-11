from random import choice

from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from categories.models import Category
from posts.models import Post


def home(request: HttpRequest) -> HttpResponse:
    last_posts = Post.objects.filter(is_active=True).order_by("-updated_at")[:5]
    most_hot = Post.objects.annotate(
        comment_count=Count("comments", distinct=True)).order_by("-comment_count").first()
    last_post = choice(last_posts)

    return render(request, "home.html", {
        "last_post": last_post,
        "most_hot": most_hot,
    })
