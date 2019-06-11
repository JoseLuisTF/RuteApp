from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.ruta.views import PuntoCreate, PuntoDelete, PuntoList, PuntoUpdate, \
    RutaCreate, RutaList, RutaUpdate, RutaDelete, RutaDetail, PuntoRutaCreate, PuntoRutaDelete, PuntoRutaUpdate, \
    RutaAsignadaDelete, RutaAsignadaCreate


urlpatterns = [
    path('puntoCrear', login_required(PuntoCreate.as_view()), name='punto_crear'),
    path('puntoListar', login_required(PuntoList.as_view()), name='punto_listar'),
    path('puntoActualizar/<pk>', login_required(PuntoUpdate.as_view()), name='punto_actualizar'),
    path('puntoEliminar/<pk>', login_required(PuntoDelete.as_view()), name='punto_eliminar'),
    path('crear', login_required(RutaCreate.as_view()), name='ruta_crear'),
    path('listar', login_required(RutaList.as_view()), name='ruta_listar'),
    path('actualizar/<pk>', login_required(RutaUpdate.as_view()), name='ruta_actualizar'),
    path('eliminar/<pk>', login_required(RutaDelete.as_view()), name='ruta_eliminar'),
    path('detalles/<pk>', login_required(RutaDetail.as_view()), name='ruta_detalles'),
    path('asignarPunto/<pk>', login_required(PuntoRutaCreate.as_view()), name='punto_asignar'),
    path('puntoRutaActualizar/<pk>', login_required(PuntoRutaUpdate.as_view()), name='puntoRuta_actualizar'),
    path('puntoRutaEliminar/<pk>', login_required(PuntoRutaDelete.as_view()), name='puntoRuta_eliminar'),
    path('rutaAsignadaEliminar/<pk>', login_required(RutaAsignadaDelete.as_view()), name='rutaAsignada_eliminar'),
    path('rutaAsignadaCrear/<pk>', login_required(RutaAsignadaCreate.as_view()), name='rutaAsignada_crear'),

]
