from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import LogInForm, SignUpForm


class SignUpView(View):
    template_name = "users/signup.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, self.template_name, {"form": form})


class LogInView(View):
    template_name = "users/login.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        form = LogInForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LogInForm((request,), data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

        return render(request, self.template_name, {"form": form})
