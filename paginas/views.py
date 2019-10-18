from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('<h1><b>Hello,</b></h1> Wooooooooorld!')

def sobreView(request):
    return HttpResponse('Página Sobre!')