from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from apps.propietario.models import PropietarioVehiculo, Propietario
from apps.vehiculo.forms import VehiculoForm
from apps.vehiculo.models import Vehiculo


# Create your views here.


class VehiculoList(ListView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_list.html'


class VehiculoCreate(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_listar')


class VehiculoUpdate(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_listar')


class VehiculoDetail(DetailView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_details.html'

    def get_context_data(self, **kwargs):
        context = super(VehiculoDetail, self).get_context_data(**kwargs)
        context['propietarios'] = PropietarioVehiculo.objects.filter(vehiculo_id=self.kwargs['pk'])
        propietario = PropietarioVehiculo.objects.filter(vehiculo_id=self.kwargs['pk']).first()
        if propietario:
            cedula = propietario.propietario_id
            context['duenios'] = Propietario.objects.filter(cedula=cedula)
        return context


class VehiculoDelete(DeleteView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_delete.html'
    success_url = reverse_lazy('vehiculo_listar')