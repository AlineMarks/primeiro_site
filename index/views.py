from django.shortcuts import render

def index (request):
    return render (request, 'arquivo/index.html', context = {'name': 'Aline Costa'})
