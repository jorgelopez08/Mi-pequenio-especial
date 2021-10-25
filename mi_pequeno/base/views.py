from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")


def quienes_somos(request):
    data = {
        "titulo": "¿Quiénes somos?",
        "texto": [
            """En la zona metropolitana de la ciudad de Guadalajara no existía ninguna 
            guardería que trabaje en la atención de niños y jóvenes con discapacidad , las que existen  
            reciben algunos niños entre las edades de 45 días de nacidos hasta los 3 años 11 meses años 
            de edad y con ciertas restricciones o al terminar el preescolar y después de eso los padres 
            de familia (principalmente mamás solteras o abandonadas) se encuentran en la problemática de 
            quién puede cuidar a su hijo (a) en todos los aspectos desde cuestiones de integridad,  psicológicos, 
            nutricionales, conductuales, etc.""",
            """Por tal motivo nace ESTA GUARDERIA, donde el personal que labora contamos con la experiencia en 
            trabajar con ésta población  y conocemos todas sus necesidades tanto de él alumno,  como el de la familia.
            """
        ],
        "img":'img/afiliacion.jpg'
    }
    return render(request, "main.html", context=data)

""" def que_hacemos(request):
    data = {
        "titulo": "Qué hacemos",
        "texto": ""
    }
    return render(request, "main.html", context=data) """

def galeria(request):
    return render(request, "galeria.html")

def contacto(request):
    data = {
        "titulo": "Contacto"
    }
    return render(request, "main.html", context=data)

def donacion(request):
    data = {
        "titulo": "Donación"
    }
    return render(request, "main.html", context=data)