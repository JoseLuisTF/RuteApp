from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.chofer.views import ChoferCreate, ChoferList, ChoferDetail, ChoferUpdate, ChoferDelete, \
    AsignacionCreate, AsignacionDelete, AsignacionHorarioCreate, AsignacionHorarioUpdate

urlpatterns = [
    path('registrar', login_required(ChoferCreate.as_view()), name='chofer_registrar'),
    path('listar', login_required(ChoferList.as_view()), name='chofer_listar'),
    path('detalles/<pk>/', login_required(ChoferDetail.as_view()), name='chofer_detalles'),
    path('actualizar/<pk>/', login_required(ChoferUpdate.as_view()), name='chofer_actualizar'),
    path('eliminar/<pk>/', login_required(ChoferDelete.as_view()), name='chofer_eliminar'),
    path('asignar/<pk>/', login_required(AsignacionCreate.as_view()), name='chofer_asignar'),
    path('eliminarAsignacion/<pk>/', login_required(AsignacionDelete.as_view()), name='chofer_eliminarAsignacion'),
    path('asignarHorario/<pk>/', login_required(AsignacionHorarioCreate.as_view()), name='chofer_asignarHorario'),
    path('actualizarHorario/<pk>/', login_required(AsignacionHorarioUpdate.as_view()), name='chofer_actualizarHorario'),

]
