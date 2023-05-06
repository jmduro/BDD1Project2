# Generated by Django 4.1.9 on 2023-05-06 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_usuarioautenticable_rol_and_more'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Login.rol'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Login.rol'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Login.rol'),
        ),
    ]
