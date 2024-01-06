import uuid

from django.db import models, IntegrityError
from django.utils.text import slugify


class SlugModel(models.Model):
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # Check if slug is unique
        # If not, append a random string to the slug
        while True:
            try:
                super().save(*args, **kwargs)
                break
            except IntegrityError:
                self.slug += f"-{uuid.uuid4().hex[:4]}"
