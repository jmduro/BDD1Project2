from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect, reverse
from .forms import CustomeCreationEdificioForm
from django.http import HttpResponse

# Create your views here.

class EdificioView(generic.CreateView):
    template_name = "edificio/edificioCrear.html"
    form_class = CustomeCreationEdificioForm

    def get_success_url(self):
        return reverse('edificio')

def EdificioPage(request):
    return render(request, 'edificio/edificio.html')