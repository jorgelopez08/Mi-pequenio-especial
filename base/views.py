from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")

def quienes_somos(request):
    return render(request, "about.html")

def que_hacemos(request):
    return render(request, "about.html")

def galeria(request):
    return render(request, "galeria.html")

def contacto(request):
    return render(request, "contact/contact.html")

def donacion(request):
    return render(request, "main.html")
