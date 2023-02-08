from django.shortcuts import render
from django.http import HttpResponse

def sobre_nos (request):
    return render (request, "sobre_nos/sobre_nos.html")
    