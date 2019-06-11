from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.vehiculo.views import VehiculoList, VehiculoCreate, VehiculoUpdate, VehiculoDetail, VehiculoDelete

urlpatterns = [
    path('listar', login_required(VehiculoList.as_view()), name='vehiculo_listar'),
    path('agregar', login_required(VehiculoCreate.as_view()), name='vehiculo_crear'),
    path('actualizar/<pk>', login_required(VehiculoUpdate.as_view()), name='vehiculo_actualizar'),
    path('detalles/<pk>', login_required(VehiculoDetail.as_view()), name='vehiculo_detalles'),
    path('eliminar/<pk>', login_required(VehiculoDelete.as_view()), name='vehiculo_eliminar'),





]

