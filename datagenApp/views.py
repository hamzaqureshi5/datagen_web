from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import TextFile
import json

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in.")
            return redirect('document')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  # Replace 'login' with the name of your login page URL pattern
    
    return render(request, 'datagenApp/login.html')  # Replace 'login.html' with the name of your login template


@login_required
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


@login_required
def keys(request):
    return render(request, "datagenApp/keys.html")


@login_required
def electrical(request):
    return render(request, "datagenApp/electrical.html")


@login_required
def graphical(request):
    return render(request, "datagenApp/graphical.html")


@login_required
def preview(request):
    return render(request, "datagenApp/preview.html")


