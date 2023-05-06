from django.db import migrations


def roles_iniciales(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Rol = apps.get_model("Login", "Rol")
    Rol.objects.create(nombre='Administrador',
                       descripcion='Tiene todos los permisos',
                       administrar_carreras=True,
                       administrar_cursos=True,
                       administrar_estudiantes=True,
                       administrar_docentes=True,
                       administrar_usuarios=True,
                       validar_cargas_academicas=True,
                       administrar_roles_y_permisos=True,
                       administracion_de_edificios_y_salones=True,
                       )
    Rol.objects.create(nombre='Personal Admin',
                       descripcion='Gestión del sistema',
                       administrar_carreras=True,
                       administrar_cursos=True,
                       administrar_estudiantes=True,
                       administrar_docentes=True,
                       administrar_usuarios=True,
                       )
    Rol.objects.create(nombre='Estudiante', descripcion='Consulta notas')

class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(roles_iniciales)
    ]
