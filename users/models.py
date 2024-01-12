from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class ForumUser(AbstractUser):
    bio = RichTextUploadingField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
