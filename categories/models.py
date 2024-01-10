from django.db import models

from core.models import SlugModel


class MainCategory(models.Model):
    title = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    class Meta:
        db_table = "main_categories"
        verbose_name = "Main Category"
        verbose_name_plural = "Main Categories"
        ordering = ["order"]

    def __str__(self) -> str:
        return self.title


class Category(SlugModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name="categories")

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
