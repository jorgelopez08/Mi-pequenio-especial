
from django.urls import path
from . import views as base_views

urlpatterns = [
    path('home/', base_views.home, name= "home"),
]
