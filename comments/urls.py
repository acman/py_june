from django.urls import path

from comments.views import CreateCommentView

app_name = "comments"

urlpatterns = [
    path("create/<slug:post_slug>/", CreateCommentView.as_view(), name="create"),
]
