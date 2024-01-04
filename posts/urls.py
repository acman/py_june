from django.urls import path

from posts.views import CreatePostView, DetailsPostView

from posts.views import CreatePostView


app_name = "posts"

urlpatterns = [
    path("create/<int:category_id>/", CreatePostView.as_view(), name="create"),

    path("details/<int:post_id>/", DetailsPostView.as_view(), name="details"),

]
