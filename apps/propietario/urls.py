from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.propietario.views import PropietarioList, PropietarioUpdate, \
    PropietarioCreate, PropietarioDetail, PropietarioVehiculoCreate, PropietarioDelete

urlpatterns = [
    path('listar', login_required(PropietarioList.as_view()), name='propietario_listar'),
    path('agregar', login_required(PropietarioCreate.as_view()), name='propietario_crear'),
    path('actualizar/<pk>', login_required(PropietarioUpdate.as_view()), name='propietario_actualizar'),
    path('detalles/<pk>', login_required(PropietarioDetail.as_view()), name='propietario_detalles'),
    path('eliminar/<pk>', login_required(PropietarioDelete.as_view()), name='propietario_eliminar'),
    path('asignarVehiculo/<pk>', login_required(PropietarioVehiculoCreate.as_view()), name='propietarioVehiculo_crear'),
]
