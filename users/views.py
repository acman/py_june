from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import SignUpForm


class SignUpView(View):
    template_name = "users/signup.html"

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, self.template_name, {"form": form})
