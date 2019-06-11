from django.contrib import admin

from apps.chofer.models import TipoChofer,Chofer, Licencia, ChoferVehiculo, TipoHorario, ChoferVehiculoHorario

# Register your models here.

admin.site.register(TipoChofer)
admin.site.register(Chofer)
admin.site.register(Licencia)
admin.site.register(ChoferVehiculo)
admin.site.register(TipoHorario)
admin.site.register(ChoferVehiculoHorario)
