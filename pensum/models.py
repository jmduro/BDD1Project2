from django.db import models
#from usuarios import models as usuario_model

# Create your models here.
class Carrera(models.Model):
    ciclos = (
        ('Semestral', 'Semestral'),
        ('Trimestral', 'Trimestral'),
        ('Anual', 'Anual')
    )
    grados = (
        ('Técnico', 'Técnico'),
        ('Licenciatura', 'Licenciatura'),
        ('Diplomado', 'Diplomado'),
        ('Especialidad', 'Especialidad'),
        ('Maestría', 'Maestría'),
        ('Doctorado', 'Doctorado'),
    )
    planes = (
        ('Matutina', 'Matutina'),
        ('Vespertina', 'Vespertina'),
        ('Nocturna', 'Nocturna'),
        ('Sábados', 'Sábados'),
        ('Domingos', 'Domingos'),
    )
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField(default=50)
    clasificacion = models.CharField(max_length=15)
    partida = models.CharField(max_length=15)
    ciclo_academico = models.CharField(choices=ciclos, max_length=100)
    grado_academico = models.CharField(choices=grados, max_length=100)
    jornada = models.CharField(choices=planes, max_length=100)
    #encargado_area = models.ForeignKey(usuario_model.Docente, on_delete=models.CASCADE)
    #coordinador_academico = models.ForeignKey(usuario_model.Docente, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"
    

class Curso(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    horas_semana = models.IntegerField(default=3)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    laboratorio = models.BooleanField(default=False)
    codigo_lab = models.CharField(max_length=10)
    horas_lab = models.IntegerField(default=0)
    semestres = models.IntegerField(default=2)
    habilitado = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Pensum(models.Model):
    codigo = models.CharField(max_length=4)
    inicio = models.IntegerField(default=2023)
    creacion = models.DateField()
    proceso = models.CharField(max_length=250)
    ciclos = models.IntegerField(default=2)
    examen = models.IntegerField(default=100)
    habilitado = models.BooleanField(default=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo}"

class Ciclo(models.Model):
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)
    ciclo = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.ciclo}"
    

class CursoPensum(models.Model):
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='nombre_curso')
    creditos = models.IntegerField(default=4)
    obligatorio = models.BooleanField(default=True)
    curso_prerrequisito = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='curso_prerrequisito')
    creditos_prerrequisito = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.curso}"