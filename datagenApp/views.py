from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib import messages

# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


################ login forms###################################################
# def Login(request):
#     if request.method == "POST":

#         # AuthenticationForm_can_also_be_used__

#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             form = login(request, user)
#             messages.success(request, f" welcome {username} !!")
#             return redirect("index")
#         else:
#             messages.info(request, f"account done not exit plz sign in")
#     form = AuthenticationForm()
#     return render(request, "user/login.html", {"form": form, "title": "log in"})


def login(request):
    return render(request, "datagenApp/login.html")


def keys(request):
    return render(request, "datagenApp/keys.html")


def electrical(request):
    return render(request, "datagenApp/electrical.html")


def graphical(request):
    return render(request, "datagenApp/graphical.html")


def preview(request):
    return render(request, "datagenApp/preview.html")


def document(request):
    return render(request, "datagenApp/document.html")
