from django.contrib import admin

from apps.ruta.models import TipoPunto, Punto, Ruta, PuntoRuta

# Register your models here.

admin.site.register(TipoPunto)
admin.site.register(Punto)
admin.site.register(Ruta)
admin.site.register(PuntoRuta)
