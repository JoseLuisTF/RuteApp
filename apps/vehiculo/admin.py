from django.contrib import admin

from apps.vehiculo.models import Vehiculo,TipoVehiculo

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(TipoVehiculo)