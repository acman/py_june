from django.urls import path

from posts.views import CreatePostView, DeletePostView, DetailsPostView, UpdatePostView

app_name = "posts"

urlpatterns = [
    path("create/<int:category_id>/", CreatePostView.as_view(), name="create"),
    path("<int:pk>/delete/", DeletePostView.as_view(), name="delete"),
    path("details/<int:post_id>/", DetailsPostView.as_view(), name="details"),
    path("<int:pk>/update/", UpdatePostView.as_view(), name="update"),
]
