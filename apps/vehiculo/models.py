from django.db import models

# Create your models here.


class TipoVehiculo(models.Model):
    id_tipo_vehiculo = models.AutoField(primary_key=True)
    nom_tipo_vehiculo = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.nom_tipo_vehiculo)


class Vehiculo(models.Model):

    placa = models.CharField(primary_key=True, max_length=6)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    anio = models.IntegerField()
    nPuertas = models.IntegerField()
    capacidad = models.IntegerField()
    num_motor = models.CharField(max_length=20)
    num_chasis = models.CharField(max_length=20)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.placa)
