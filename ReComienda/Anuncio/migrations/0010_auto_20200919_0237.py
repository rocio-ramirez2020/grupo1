# Generated by Django 3.1.1 on 2020-09-19 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Anuncio', '0009_auto_20200918_2245'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Anuncio_Transportista',
            new_name='Anuncio_Trans',
        ),
        migrations.RemoveField(
            model_name='contratista',
            name='tipo_servicio',
        ),
        migrations.DeleteModel(
            name='Servicios',
        ),
    ]
