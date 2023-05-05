from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render(request, 'main/inicio.html')

def EdificioPage(request):
    return render(request, 'edificio/edificio.html')