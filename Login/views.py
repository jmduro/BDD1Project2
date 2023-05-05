from django.shortcuts import render
from django.views import generic
from .forms import CustomeCreationUserForm, RolForm, RolForm2, RolForm3
from django.shortcuts import render,redirect,reverse
from django.core.mail import send_mail
from .models import Rol
from django.http import HttpResponse

# Create your views here.

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomeCreationUserForm

    def get_success_url(self):
        return reverse("login")

def HomePage(request):
    return render(request, 'main/inicio.html')

def LoginPage(request):
    return render(request, 'main/login.html')
    
def RolPage(request):
    roles= Rol.objects.all()
    context = {
        'roles':roles
    }
    return render(request, 'main/roles.html',context)

def RolCreate(request):
    form=RolForm()
    if request.method == "POST":
        form = RolForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            Rol.objects.create(
                nombre=nombre,
                descripcion=descripcion
        )
        return redirect('roles')
    context = {
        'form':form
    }
    return render(request, 'main/rol_create.html', context)

def RolUpdate(request,pk):
    rol = Rol.objects.get(id=pk)
    form=RolForm2(instance=rol)
    if request.method == "POST":
        form = RolForm2(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('roles')
    context = {
        'form':form,
        "rol":rol
    }
    return render(request,"main/rol_update.html", context)

def RolModificar(request,pk):
    rol = Rol.objects.get(id=pk)
    form=RolForm3(instance=rol)
    if request.method == "POST":
        form = RolForm3(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('roles')
    context = {
        'form':form,
        "rol":rol
    }
    return render(request,"main/rol_modificar.html", context)

