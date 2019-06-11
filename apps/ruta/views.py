from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from apps.ruta.forms import PuntoForm, RutaForm, PuntoRutaForm, RutaAsignadaForm
from apps.ruta.models import Punto, Ruta, PuntoRuta, RutaAsignada


# Create your views here.


class PuntoDelete(DeleteView):
    model = Punto
    template_name = 'ruta/punto_delete.html'
    success_url = reverse_lazy('punto_listar')


class PuntoList(ListView):
    model = Punto
    template_name = 'ruta/punto_list.html'


class PuntoCreate(CreateView):
    model = Punto
    form_class = PuntoForm
    template_name = 'ruta/punto_form.html'
    success_url = reverse_lazy('punto_listar')


class PuntoUpdate(UpdateView):
    model = Punto
    form_class = PuntoForm
    template_name = 'ruta/punto_form.html'
    success_url = reverse_lazy('punto_listar')


class RutaDelete(DeleteView):
    model = Ruta
    template_name = 'ruta/ruta_delete.html'
    success_url = reverse_lazy('punto_listar')


class RutaList(ListView):
    model = Ruta
    template_name = 'ruta/ruta_list.html'


class RutaCreate(CreateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'ruta/ruta_form.html'
    success_url = reverse_lazy('ruta_listar')


class RutaUpdate(UpdateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'ruta/ruta_form.html'
    success_url = reverse_lazy('ruta_listar')


class RutaDetail(DetailView):
    model = Ruta
    template_name = 'ruta/ruta_details.html'

    def get_context_data(self, **kwargs):
        context = super(RutaDetail, self).get_context_data(**kwargs)
        context['puntos'] = PuntoRuta.objects.filter(ruta_id=self.kwargs['pk'])
        context['asignados'] = RutaAsignada.objects.filter(ruta_id=self.kwargs['pk'])

        return context


class PuntoRutaCreate(CreateView):
    model = PuntoRuta
    form_class = PuntoRutaForm
    template_name = 'ruta/puntoRuta_form.html'
    success_url = reverse_lazy('ruta_listar')

    def form_valid(self, form):
        form.instance.ruta = Ruta.objects.filter(id_ruta=self.kwargs['pk']).first()
        return super(PuntoRutaCreate, self).form_valid(form)


class PuntoRutaUpdate(UpdateView):
    model = PuntoRuta
    form_class = PuntoRutaForm
    template_name = 'ruta/puntoRuta_form.html'
    success_url = reverse_lazy('ruta_listar')


class PuntoRutaDelete(DeleteView):
    model = PuntoRuta
    template_name = 'ruta/puntoRuta_delete.html'
    success_url = reverse_lazy('ruta_listar')


class RutaAsignadaDelete(DeleteView):
    model = RutaAsignada
    template_name = 'ruta/rutaAsignada_delete.html'
    success_url = reverse_lazy('ruta_listar')


class RutaAsignadaCreate(CreateView):
    model = RutaAsignada
    form_class = RutaAsignadaForm
    template_name = 'ruta/rutaAsignada_form.html'
    success_url = reverse_lazy('ruta_listar')

    def form_valid(self, form):
        form.instance.ruta = Ruta.objects.filter(id_ruta=self.kwargs['pk']).first()
        return super(RutaAsignadaCreate, self).form_valid(form)
