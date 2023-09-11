from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(request):
    html="""
    <h1 style='color:blue'>Bienvenido! vista 1 de la app1</h1>
    <a href="/vista2">Ver vista 2</a>
    
    """
    return HttpResponse(html)


def vista2(request):
    html="""
    <h1 style='color:red'>Bienvenido a la vista 2</h1>
    <a href="http://127.0.0.1:8000/">Volver</a>
    
    """
    return HttpResponse(html)    
