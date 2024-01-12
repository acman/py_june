from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from core.models import SlugModel


class Post(SlugModel):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField(default="", blank=True, null=True)
    author = models.ForeignKey(
        "users.ForumUser", on_delete=models.CASCADE, related_name="posts"
    )
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title
