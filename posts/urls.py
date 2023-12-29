from django.urls import path

from posts.views import CreatePostView

app_name = "posts"

urlpatterns = [
    path("create/<int:category_id>/", CreatePostView.as_view(), name="create"),
]
