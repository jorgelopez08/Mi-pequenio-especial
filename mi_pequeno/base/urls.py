
from django.urls import path
from . import views as base_views

urlpatterns = [
    path('', base_views.home, name= "home"),
    path('quienes-somos/', base_views.quienes_somos, name='quien_somos'),
    #path('que-hacemos/', base_views.que_hacemos, name='que_hacemos'),
    path('galeria/', base_views.galeria, name='galeria'),
    path('contacto/', base_views.contacto, name='contacto'),
    path('donacion/', base_views.donacion, name='donacion'),
]
