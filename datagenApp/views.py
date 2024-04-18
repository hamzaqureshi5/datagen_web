from django.shortcuts import render


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
