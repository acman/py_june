import uuid

from django.db import IntegrityError, models
from django.utils.text import slugify
from unidecode import unidecode


class SlugModel(models.Model):
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        abstract = True

    def save(self, *args: tuple, **kwargs: dict) -> None:
        if not self.slug:
            self.slug = slugify(unidecode(self.title))

        # Check if slug is unique
        # If not, append a random string to the slug
        while True:
            try:
                super().save(*args, **kwargs)
                break
            except IntegrityError:
                self.slug += f"-{uuid.uuid4().hex[:4]}"
