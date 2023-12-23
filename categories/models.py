from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
