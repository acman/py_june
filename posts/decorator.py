from django.shortcuts import redirect


def user_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("users:login")
        return view_func(request, *args, **kwargs)
    return wrapper
