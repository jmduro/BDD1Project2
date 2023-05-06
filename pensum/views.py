from django.shortcuts import render, redirect

from .models import Curso, Carrera, Pensum, Ciclo, CursoPensum
from .forms import CarreraModelForm, CursoModelForm, PensumModelForm, CicloModelForm, CursoPensumModelForm

#--------- ESPACIO DE CARRERAS ---------

def carrera(request):
    carreras = Carrera.objects.all()
    context = {
        "carreras" : carreras
    }
    return render(request, "pensum/carrera.html", context)

def crear_carrera(request):
    form = CarreraModelForm()
    if request.method == "POST":
        form = CarreraModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/inicio/pensum/carrera")
    context = {
        "form": form
    }
    return render(request, "pensum/crear_carrera.html", context)

def editar_carrera(request, pk):
    carrera = Carrera.objects.get(id=pk)
    form = CarreraModelForm(instance=carrera)
    if request.method == "POST":
        form = CarreraModelForm(request.POST, instance=carrera)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/inicio/pensum/carrera")
    context = {
        "form" : form,
        "carrera" : carrera
    }
    return render(request, "pensum/editar_carrera.html", context)


#--------- ESPACIO DE CURSOS ---------

def curso(request):
    cursos = Curso.objects.all()
    context = {
        "cursos" : cursos
    }
    return render(request, "pensum/curso.html", context)

def crear_curso(request):
    form = CursoModelForm()
    if request.method == "POST":
        form = CursoModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/inicio/pensum/curso")
    context = {
        "form": CursoModelForm()
    }
    return render(request, "pensum/crear_curso.html", context)

def editar_curso(request, pk):
    curso = Curso.objects.get(id=pk)
    form = CursoModelForm(instance=curso)
    if request.method == "POST":
        form = CursoModelForm(request.POST, instance=curso)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/inicio/pensum/curso")
    context = {
        "form" : form,
        "curso" : curso
    }
    return render(request, "pensum/editar_curso.html", context)


#--------- ESPACIO DE PENSUM ---------

def pensum(request, pk):
    carrera = Carrera.objects.get(id=pk)
    pensum = Pensum.objects.filter(carrera=carrera.pk)
    print(pensum)
    context = {
        "carrera" : carrera,
        "pensum" : pensum
    }
    return render(request, "pensum/pensum.html", context)

def crear_pensum(request):
    form = PensumModelForm()
    if request.method == "POST":
        form = PensumModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/inicio/pensum/carrera")
    context = {
        "form": PensumModelForm()
    }
    return render(request, "pensum/crear_pensum.html", context)

def editar_pensum(request, pk):
    pensum = Pensum.objects.get(id=pk)
    form = PensumModelForm(instance=pensum)
    if request.method == "POST":
        form = PensumModelForm(request.POST, instance=pensum)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/inicio/pensum/carrera")
    context = {
        "form" : form,
        "pensum" : pensum
    }
    return render(request, "pensum/editar_pensum.html", context)


#--------- ESPACIO DE CICLOS ---------
def ciclo(request, pk):
    pensum = Pensum.objects.get(id=pk)
    ciclo = Ciclo.objects.filter(pensum=pensum.pk)
    context = {
        "pensum" : pensum,
        "ciclo" : ciclo
    }
    return render(request, "pensum/ciclo.html", context)


def crear_ciclo(request):
    form = CicloModelForm()
    if request.method == "POST":
        form = CicloModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/inicio/pensum/carrera")
    context = {
        "form": CicloModelForm()
    }
    return render(request, "pensum/crear_ciclo.html", context)


#--------- ESPACIO DE CURSOS PARA PENSUM ---------
def curso_pensum(request, pk):
    ciclo = Ciclo.objects.get(id=pk)
    curso_pensum = CursoPensum.objects.filter(ciclo=ciclo.pk)
    context = {
        "ciclo" : ciclo,
        "curso_pensum" : curso_pensum
    }
    return render(request, "pensum/curso_pensum.html", context)

def agregar_curso(request):
    form = CursoPensumModelForm()
    if request.method == "POST":
        form = CursoPensumModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/inicio/pensum/carrera")
    context = {
        "form": CursoPensumModelForm()
    }
    return render(request, "pensum/agregar_curso.html", context)

def editar_curso_pensum(request, pk):
    curso = CursoPensum.objects.get(id=pk)
    form = CursoPensumModelForm(instance=curso)
    if request.method == "POST":
        form = CursoPensumModelForm(request.POST, instance=curso)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/inicio/pensum/carrera")
    context = {
        "form" : form,
        "curso" : curso
    }
    return render(request, "pensum/editar_curso_pensum.html", context)