# Generated by Django 4.2 on 2023-05-05 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edificios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salon_clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('habilitado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('capacidad', models.IntegerField(default=0)),
                ('habilitado', models.BooleanField(default=True)),
                ('Salon_clasificacion', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='edificios.salon_clasificacion')),
                ('edificio', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='edificios.edificio')),
            ],
        ),
    ]
