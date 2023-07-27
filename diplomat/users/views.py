from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home_view(request):
    return render(request, "users_home.html")


def logout_view(request):
    logout(request)
    return redirect("users/")
