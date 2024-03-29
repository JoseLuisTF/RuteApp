# Generated by Django 2.2.2 on 2019-06-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chofer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id_punto', models.AutoField(primary_key=True, serialize=False)),
                ('nom_punto', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id_ruta', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_ruta', models.CharField(max_length=35)),
                ('resolucion', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPunto',
            fields=[
                ('id_tipo_punto', models.AutoField(primary_key=True, serialize=False)),
                ('nom_tipo_punto', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RutaAsignada',
            fields=[
                ('id_ruta_asignada', models.AutoField(primary_key=True, serialize=False)),
                ('chofer_vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chofer.ChoferVehiculo')),
                ('ruta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.Ruta')),
            ],
        ),
        migrations.CreateModel(
            name='PuntoRuta',
            fields=[
                ('id_punto_ruta', models.AutoField(primary_key=True, serialize=False)),
                ('punto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.Punto')),
                ('ruta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.Ruta')),
                ('tipo_punto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.TipoPunto')),
            ],
        ),
    ]
