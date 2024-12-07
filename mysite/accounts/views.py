from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    """
    Authenticates users and redirects to the index page on successful login, or shows an error message on failure.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("website:index")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "accounts/login.html")


def logout_view(request):
    """
    Logs out the current user and redirects to the login page.
    """
    logout(request)
    return redirect("accounts:login")


def signup_view(request):
    """
    Registers a new user, logs them in on success, and redirects to the index page or shows an error for existing usernames.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            login(request, user)
            return redirect("website:index")
    return render(request, "accounts/signup.html")
