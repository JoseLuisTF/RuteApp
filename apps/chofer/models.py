from django.db import models

from apps.vehiculo.models import Vehiculo


# Create your models here.


class TipoChofer (models.Model):
    id_tipo_chofer = models.AutoField(primary_key=True)
    nom_tipo_chofer = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.nom_tipo_chofer)


class Chofer (models.Model):

    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    tipo_chofer = models.ForeignKey(TipoChofer, null=True, blank=True, on_delete=models.CASCADE)


class Licencia (models.Model):

    num_licencia = models.CharField(primary_key=True, max_length=10)
    categoria = models.CharField(max_length=2)
    fec_expedicion = models.DateField()
    fec_vencimiento = models.DateField()
    oficia_expedida = models.CharField(max_length=30)
    chofer = models.ForeignKey(Chofer, null=True, blank=True, on_delete=models.CASCADE)


class ChoferVehiculo (models.Model):

    id_chofer_vehiculo = models.AutoField(primary_key=True)
    vehiculo = models.OneToOneField(Vehiculo, null=True, blank=True, on_delete=models.CASCADE)
    chofer = models.OneToOneField(Chofer, null=True, blank=True, on_delete=models.SET_NULL)
    fecha_asignacion = models.DateField()

    def __str__(self):
        return '{}'.format(self.chofer_id + ' ' +  self.vehiculo_id)


class TipoHorario (models.Model):

    id_horario = models.AutoField(primary_key=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.descripcion)


class ChoferVehiculoHorario (models.Model):

    id_chofer_vehiculo_horario = models.AutoField(primary_key=True)
    chofer_vehiculo = models.ForeignKey(ChoferVehiculo, null=True, blank=True, on_delete=models.CASCADE)
    horario_turno = models.ForeignKey(TipoHorario, null=True, blank=True, on_delete=models.CASCADE)



