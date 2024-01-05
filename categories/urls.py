from django.urls import path

from categories import views

app_name = "categories"

urlpatterns = [
    path("category_list/", views.category_list, name="list"),
    path("category_detail/<int:category_id>/", views.category_detail, name="detail"),
]
