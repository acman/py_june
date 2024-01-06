from django.urls import path

from posts.views import CreatePostView, DeletePostView, DetailsPostView, UpdatePostView

app_name = "posts"

urlpatterns = [
    path("create/<slug:category_slug>/", CreatePostView.as_view(), name="create"),
    path("<slug:post_slug>/delete/", DeletePostView.as_view(), name="delete"),
    path("details/<slug:post_slug>/", DetailsPostView.as_view(), name="details"),
    path("<slug:post_slug>/update/", UpdatePostView.as_view(), name="update"),
]
