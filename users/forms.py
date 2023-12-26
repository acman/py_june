from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ForumUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=127, help_text="Required. Enter valid email address")

    class Meta:
        model = ForumUser
        fields = ["username", "email", "password1", "password2"]
