from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(request):
    html="""
    <h1>Bienvenido a la vista 1!</h1>
    <a href="/vista2">Vista 2</a>
    """
    return HttpResponse(html)

def vista2(request):
    html="""
    <h1>Bienvenido a la vista 2!</h1>
    <a href="http://127.0.0.1:8000/">Volver</a>
    """
    return HttpResponse(html)
