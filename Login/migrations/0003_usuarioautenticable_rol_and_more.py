# Generated by Django 4.1.9 on 2023-05-06 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20230505_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioautenticable',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Login.rol'),
        ),
        migrations.AlterField(
            model_name='rol',
            name='administracion_de_edificios_y_salones',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rol',
            name='administrar_carreras',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rol',
            name='administrar_cursos',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rol',
            name='administrar_docentes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rol',
            name='administrar_estudiantes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rol',
            name='administrar_roles_y_permisos',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rol',
            name='administrar_usuarios',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rol',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='rol',
            name='validar_cargas_academicas',
            field=models.BooleanField(default=False),
        ),
    ]
