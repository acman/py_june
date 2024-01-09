from django.urls import path

from comments.views import CreateCommentView, UpdateCommentView

app_name = "comments"

urlpatterns = [
    path("create/<slug:post_slug>/", CreateCommentView.as_view(), name="create"),
    path(
        "update/<slug:post_slug>/<int:comment_pk>/",
        UpdateCommentView.as_view(),
        name="update",
    ),
]
