from django.db import models

from core.models import SlugModel


class Comment(SlugModel):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500, blank=True)
    author = models.ForeignKey("users.ForumUser", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "comments"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title
