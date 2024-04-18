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
from .models import TextFile

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

# def upload_text_file(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         uploaded_file = request.FILES['file']
#         text_file = TextFile(file=uploaded_file)
#         text_file.file_path = uploaded_file.name
#         text_file.save()
#         return redirect('upload_success')
#     return render(request, 'upload_text_file.html')

def document(request):
    context = {'result':"Sucessfully uploaded!"}
    print("--------------------->This message will be printed in the console or terminal where Django server is running.")

    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        text_file = TextFile(file=uploaded_file)
        text_file.file_path = uploaded_file.name
        text_file.save()
    context = {'result':"Error loading file!"}

    return render(request, "datagenApp/document.html", context)

def keys(request):
    return render(request, "datagenApp/keys.html")


def electrical(request):
    return render(request, "datagenApp/electrical.html")


def graphical(request):
    return render(request, "datagenApp/graphical.html")


def preview(request):
    return render(request, "datagenApp/preview.html")


