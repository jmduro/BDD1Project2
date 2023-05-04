from django.shortcuts import render
from django.views import generic
from .forms import CustomCreationUserForm
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
# Create your views here.


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomCreationUserForm

    def get_success_url(self):
        return reverse("login")


def HomePage(request):
    return render(request, 'main/inicio.html')


def LoginPage(request):
    return render(request, 'main/login.html')
