from django.urls import path

from posts.views import CreatePostView, DeletePostView, DetailsPostView, UpdatePostView

app_name = "posts"

urlpatterns = [
    path("create/<slug:category_slug>/", CreatePostView.as_view(), name="create"),
    path("delete/<slug:post_slug>/", DeletePostView.as_view(), name="delete"),
    path("update/<slug:post_slug>/", UpdatePostView.as_view(), name="update"),
    path("<slug:post_slug>/", DetailsPostView.as_view(), name="details"),
]
