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
    SecurityKeysRandomization,
    ElectricalDataJson,
    GraphicalDataJson,
    Zong_Input_Dataframe,
    ElectricalOutputData,
)
from .utils import (
    save_keys,
    save_electrical_data,
    save_graphical_data,
    save_uploaded_file,
    preview_files_gets,
)
import json
from app.datagen.STCAppScriptV6 import *


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
            return redirect("login")

    return render(request, "datagenApp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@login_required
def document(request):
    context = {"result": "Sucessfully uploaded!", "success": False}
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        try:
            save_uploaded_file(uploaded_file)
            context["result"] = str("File uploaded successfully")
            context["success"] = True

        except Exception as e:
            context["result"] = str(e)
            context["success"] = False

    return render(request, "datagenApp/document.html", context)


@csrf_exempt
def save_electrical(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return save_electrical_data(data)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


@csrf_exempt
def save_graphical(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return save_graphical_data(data)
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
    print("=======PREVIEW========")
    gdict = GraphicalDataJson.get_json()

    edict = ElectricalDataJson.get_json()

    e, l, g, k = preview_files_gets()
    #    df = pd.read_csv("dummy.csv", encoding="latin-1")
    df = e
    print("----> ", df)

    for index, row in df.iterrows():
        row_data = df.iloc[index]
        comma_separated = ",".join(row_data.astype(str))
        record = ElectricalOutputData(row_value=comma_separated)
        record.save()

    df_html = df.to_html()  # Convert DataFrame to HTML table
    context = {"df_html": df_html}

    return render(request, "datagenApp/preview.html", context=context)


@login_required
def generate(request):
    return render(request, "datagenApp/generate.html")
