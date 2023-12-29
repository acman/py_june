from django.contrib import admin

from categories.models import Category, MainCategory

admin.site.register(MainCategory)
admin.site.register(Category)
