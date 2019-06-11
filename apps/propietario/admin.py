from django.contrib import admin

from apps.propietario.models import Propietario, PropietarioVehiculo

# Register your models here.

admin.site.register(Propietario)
admin.site.register(PropietarioVehiculo)
