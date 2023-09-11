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
    <h1 style="font-size: 36px;
  background: -webkit-linear-gradient(#fff, #333);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;">Bienvenido a la vista 2 de la app2!</h1>
    <a href="http://127.0.0.1:8000/">Volver</a>
    """
    return HttpResponse(html)
