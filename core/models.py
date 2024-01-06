from django.db import models
from django.utils.text import slugify


class SlugModel(models.Model):
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
