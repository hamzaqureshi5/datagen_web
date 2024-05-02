from django.shortcuts import render, redirect ,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import TextFile, EncryptionKeys, StartingParams, SecurityKeys, SecurityKeysRandomization
from .utils import dg_function, save_keys

import json


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in.")
            if remember_me is not None:
                request.session.set_expiry(604800)
            return redirect("document")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect(
                "login"
            )  # Replace 'login' with the name of your login page URL pattern

    return render(
        request, "datagenApp/login.html"
    )  # Replace 'login.html' with the name of your login template


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(
        reverse("login")
    )  # Assuming 'home' is the name of your home page URL pattern


@login_required
def document(request):
    context = {"result": "Sucessfully uploaded!"}

    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        text_file = TextFile(file=uploaded_file)
        text_file.file_path = uploaded_file.name
        text_file.save()
    context = {"result": "Error loading file!"}

    return render(request, "datagenApp/document.html", context)


@login_required
def keys(request):
    context = save_keys(request)
    return render(request, "datagenApp/keys.html", context=context)


@login_required
def electrical(request):
    return render(request, "datagenApp/electrical.html")


@login_required
def graphical(request):
    return render(request, "datagenApp/graphical.html")


@login_required
def preview(request):
    return render(request, "datagenApp/preview.html")


@login_required
def generate(request):
    return render(request, "datagenApp/generate.html")
