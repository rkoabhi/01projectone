from django.shortcuts import render
from django.http import HttpResponse
def homePageview(request):
    return HttpResponse('Hola means hello in Spanish')

# Create your views here.
