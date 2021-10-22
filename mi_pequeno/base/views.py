from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")

def quienes_somos(request):
    data = {
        "titulo":"Quienes somos"
        }
    return render(request, "main.html", context=data)

def que_hacemos(request):
    data = {
        "titulo":"Qué hacemos"
        }
    return render(request, "main.html", context=data)


def galeria(request):
    return render(request, "galeria.html")

def contacto(request):
    data = {
        "titulo":"Contacto"
        }
    return render(request, "main.html", context=data)


def donacion(request):
    data = {
        "titulo":"Donación"
        }
    return render(request, "main.html", context=data)

    