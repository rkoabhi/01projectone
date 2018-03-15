

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def homePageview(request):
    return HttpResponse('Namaste means hello in Hindi')
