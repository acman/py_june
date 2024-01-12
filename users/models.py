from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.db import models


class ForumUser(AbstractUser):
    bio = RichTextUploadingField(default="", null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
