from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from apps.propietario.models import Propietario, PropietarioVehiculo
from apps.propietario.forms import PropietarioForm, PropietarioVehiculoForm


# Create your views here.


class PropietarioDelete(DeleteView):
    model = Propietario
    template_name = 'propietario/propietario_delete.html'
    success_url = reverse_lazy('propietario_listar')


class PropietarioList(ListView):
    model = Propietario
    template_name = 'propietario/propietario_list.html'


class PropietarioCreate(CreateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'propietario/propietario_form.html'
    success_url = reverse_lazy('propietario_listar')


class PropietarioUpdate(UpdateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'propietario/propietario_form.html'
    success_url = reverse_lazy('propietario_listar')


class PropietarioDetail(DetailView):
    model = Propietario
    template_name = 'propietario/propietario_details.html'

    def get_context_data(self, **kwargs):
        context = super(PropietarioDetail, self).get_context_data(**kwargs)
        context['vehiculos'] = PropietarioVehiculo.objects.filter(propietario__cedula=self.kwargs['pk'])
        return context


class PropietarioVehiculoCreate(CreateView):
    model = PropietarioVehiculo
    form_class = PropietarioVehiculoForm
    template_name = 'propietario/propietarioVehiculo_form.html'
    success_url = reverse_lazy('propietario_listar')

    def form_valid(self, form):
        form.instance.propietario = Propietario.objects.filter(cedula=self.kwargs['pk']).first()
        return super(PropietarioVehiculoCreate, self).form_valid(form)
