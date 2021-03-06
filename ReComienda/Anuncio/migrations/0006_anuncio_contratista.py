# Generated by Django 3.1.1 on 2020-09-17 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Anuncio', '0005_auto_20200917_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio_contratista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('tel', models.IntegerField()),
                ('localidad_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localidad_dstino', to='Anuncio.localidad')),
                ('localidad_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localidad_orgen', to='Anuncio.localidad')),
            ],
        ),
    ]
