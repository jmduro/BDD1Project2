# Generated by Django 4.1.9 on 2023-05-05 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.IntegerField(default=50)),
                ('clasificacion', models.CharField(max_length=15)),
                ('partida', models.CharField(max_length=15)),
                ('ciclo_academico', models.CharField(choices=[('Semestral', 'Semestral'), ('Trimestral', 'Trimestral'), ('Anual', 'Anual')], max_length=100)),
                ('grado_academico', models.CharField(choices=[('Técnico', 'Técnico'), ('Licenciatura', 'Licenciatura'), ('Diplomado', 'Diplomado'), ('Especialidad', 'Especialidad'), ('Maestría', 'Maestría'), ('Doctorado', 'Doctorado')], max_length=100)),
                ('jornada', models.CharField(choices=[('Matutina', 'Matutina'), ('Vespertina', 'Vespertina'), ('Nocturna', 'Nocturna'), ('Sábados', 'Sábados'), ('Domingos', 'Domingos')], max_length=100)),
                ('habilitado', models.BooleanField(default=True)),
                ('coordinador_academico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_coordinador_academico', to='usuarios.docente')),
                ('encargado_area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_encargado_area', to='usuarios.docente')),
            ],
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4)),
                ('inicio', models.IntegerField(default=2023)),
                ('creacion', models.DateField()),
                ('proceso', models.CharField(max_length=250)),
                ('ciclos', models.IntegerField(default=2)),
                ('examen', models.IntegerField(default=100)),
                ('habilitado', models.BooleanField(default=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('horas_semana', models.IntegerField(default=3)),
                ('laboratorio', models.BooleanField(default=False)),
                ('codigo_lab', models.CharField(max_length=10)),
                ('horas_lab', models.IntegerField(default=0)),
                ('semestres', models.IntegerField(default=2)),
                ('habilitado', models.BooleanField(default=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.carrera')),
            ],
        ),
    ]
