from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500, blank=True)
    author = models.ForeignKey("users.ForumUser", on_delete=models.CASCADE)
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE)
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
