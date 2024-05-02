from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect, HttpResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import TextFile, EncryptionKeys, StartingParams, SecurityKeys, SecurityKeysRandomization
import json


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")
        print("--------------------->", remember_me)

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
    print(
        "--------------------->This message will be printed in the console or terminal where Django server is running."
    )

    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        text_file = TextFile(file=uploaded_file)
        text_file.file_path = uploaded_file.name
        text_file.save()
    context = {"result": "Error loading file!"}

    return render(request, "datagenApp/document.html", context)


from .utils import dg_function


@login_required
def keys(request):

    #    if request.method == "POST":
    # 	customer = request.user.customer
    op = request.POST.get("op_key_text", "")
    k4 = request.POST.get("k4_key_text", "")
    si = request.POST.get("data_size_text", "")
    iccid = request.POST.get("iccid_text", "")
    imsi = request.POST.get("imsi_text", "")
    pin1 = request.POST.get("pin1_text", "")
    puk1 = request.POST.get("puk1_text", "")
    pin2 = request.POST.get("pin2_text", "")
    puk2 = request.POST.get("puk2_text", "")
    adm1 = request.POST.get("adm1_text", "")
    adm6 = request.POST.get("adm6_text", "")

    pin1_rand = request.POST.get("pin1_rand_check", False)
    puk1_rand = request.POST.get("puk1_rand_check", False)
    pin2_rand = request.POST.get("pin2_rand_check", False)
    puk2_rand = request.POST.get("puk2_rand_check", False)
    adm1_rand = request.POST.get("adm1_rand_check", False)
    adm6_rand = request.POST.get("adm6_rand_check", False)

    SecurityKeys.objects.create(
        pin1=pin1,
        puk1=puk1,
        pin2=pin2,
        puk2=puk2,
        adm1=adm1,
        adm6=adm6,
    )

    SecurityKeysRandomization.objects.create(
        pin1_rand=pin1_rand,
        puk1_rand=puk1_rand,
        pin2_rand=pin2_rand,
        puk2_rand=puk2_rand,
        adm1_rand=adm1_rand,
        adm6_rand=adm6_rand,
    )

    EncryptionKeys.objects.create(
        k4=k4,
        op=op,
    )

    StartingParams.objects.create(
        size=si,
        iccid=iccid,
        imsi=imsi,
    )

    context = {
        "K4": k4,
        "OP": op,
        "SIZE": si,
        "ICCID": iccid,
        "IMSI": imsi,
        "PIN1": pin1,
        "PIN2": pin2,
        "PUK1": puk1,
        "PUK2": puk2,
        "ADM1": adm1,
        "ADM6": adm6,
    }
    #    print("======================>", request.body)
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
