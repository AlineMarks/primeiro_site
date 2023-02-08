from django.shortcuts import render
from django.http import HttpResponse

def contatos (request):
    return render(request, "contatos/contatos.html")
