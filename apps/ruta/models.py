from django.db import models

from apps.chofer.models import ChoferVehiculo


# Create your models here.


class TipoPunto(models.Model):
    id_tipo_punto = models.AutoField(primary_key=True)
    nom_tipo_punto = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.nom_tipo_punto)


class Punto(models.Model):
    id_punto = models.AutoField(primary_key=True)
    nom_punto = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.nom_punto)


class Ruta(models.Model):
    id_ruta = models.AutoField(primary_key=True)
    descripcion_ruta = models.CharField(max_length=35)
    resolucion = models.CharField(max_length=15)


class PuntoRuta(models.Model):
    id_punto_ruta = models.AutoField(primary_key=True)
    ruta = models.ForeignKey(Ruta, null=True, blank=True, on_delete=models.CASCADE)
    punto = models.ForeignKey(Punto, null=True, blank=True, on_delete=models.CASCADE)
    tipo_punto = models.ForeignKey(TipoPunto, null=True, blank=True, on_delete=models.CASCADE)


class RutaAsignada(models.Model):
    id_ruta_asignada = models.AutoField(primary_key=True)
    ruta = models.ForeignKey(Ruta, null=True, blank=True, on_delete=models.CASCADE)
    chofer_vehiculo = models.ForeignKey(ChoferVehiculo, null=True, blank=True, on_delete=models.CASCADE)
