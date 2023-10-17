from django.shortcuts import render


# Create your views here.
from django.views.generic import TemplateView, ListView

class IndexView (TemplateView):
    template_name='empleado/home.html' #lo debemos crear en la carpeta templates

class Login(TemplateView):
    template_name='empleado/login.html'

class Productos(TemplateView):
    template_name = 'empleado/Productos.html'
