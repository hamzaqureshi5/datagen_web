from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import (
    TextFile,
    EncryptionKeys,
    StartingParams,
    SecurityKeys,
    SecurityKeysRandomization, ElectricalDataJson
)
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
            ) 

    return render(request, "datagenApp/login.html")


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(reverse("login"))


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

@csrf_exempt  # Consider CSRF protection as needed
def save_data(request):
    print ("Saving data")
    if request.method == 'POST':
        data = json.loads(request.body)
        ElectricalDataJson.objects.all().delete()
        data_objects = [
        ElectricalDataJson(parameter=item['variable'], lclip=item['clip'], rclip=item['length'])for item in data]
        ElectricalDataJson.objects.bulk_create(data_objects)
#        with open('file.json', 'w') as f:
#            json.dump(data, f, indent=4)
        return JsonResponse({"status": "success", "message": "Data saved successfully."})
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

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
