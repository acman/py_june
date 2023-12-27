from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import SignUpView, LogInView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout')
]