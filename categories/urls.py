from django.urls import path

from categories import views

app_name = "categories"

urlpatterns = [
    path("", views.category_list, name="list"),
    path("<slug:category_slug>/", views.category_detail, name="detail"),
]
