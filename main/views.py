from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>Test</h1>")

# Create your views here.
