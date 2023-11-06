from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def check(request):
    return HttpResponse("<h1>Hello, from my app!</h1>")