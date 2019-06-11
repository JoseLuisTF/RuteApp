from django.db import models
from apps.vehiculo.models import Vehiculo

# Create your models here.


class Propietario (models.Model):

    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()


class PropietarioVehiculo (models.Model):
    id_propietario_vehiculo = models.AutoField(primary_key=True)
    propietario = models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.CASCADE)
    vehiculo = models.OneToOneField(Vehiculo, null=True, blank=True, on_delete=models.CASCADE)
    fecha_compra = models.DateField()
