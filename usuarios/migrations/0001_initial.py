# Generated by Django 4.1.9 on 2023-05-05 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=50)),
                ('acronimo', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('cui', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=25)),
                ('num_personal', models.CharField(max_length=10)),
                ('habilitado', models.BooleanField(default=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_identificacion', models.CharField(max_length=30, null=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('carnet', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=25)),
                ('fecha_nacimiento', models.DateField()),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('habilitado', models.BooleanField(default=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=50)),
                ('acronimo', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('cui', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=25)),
                ('num_personal', models.CharField(max_length=10)),
                ('habilitado', models.BooleanField(default=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
