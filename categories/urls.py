from django.urls import path

from categories import views

app_name = 'categories'

urlpatterns = [
    path('category_list/', views.category_list, name='list'),
]
