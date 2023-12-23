from django.urls import path

from categories import views

urlpatterns = [
    path('category_list/', views.category_list, name='category_list'),
]
