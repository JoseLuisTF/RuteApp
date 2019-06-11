from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from apps.chofer.forms import ChoferForm, LicenciaForm, AsignacionForm, AsignacionHorarioForm
from apps.chofer.models import Chofer, Licencia, ChoferVehiculo, ChoferVehiculoHorario


# Create your views here.

class ChoferList (ListView):
    model = Chofer
    template_name = 'chofer/chofer_list.html'


class ChoferDetail(DetailView):
    model = Chofer
    template_name = 'chofer/chofer_details.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(ChoferDetail, self).get_context_data(**kwargs)
        context['licencias'] = Licencia.objects.filter(chofer_id=pk)
        context['asignados'] = ChoferVehiculo.objects.filter(chofer_id=pk)
        chofer_vehiculo = ChoferVehiculo.objects.filter(chofer_id=self.kwargs['pk']).first()
        context['horarios'] = ChoferVehiculoHorario.objects.filter(chofer_vehiculo=chofer_vehiculo)
        return context


class ChoferCreate (CreateView):
    model = Chofer
    form_class = ChoferForm
    second_form_class = LicenciaForm
    template_name = 'chofer/chofer_form.html'
    success_url = reverse_lazy('chofer_listar')

    def get_context_data(self, **kwargs):
        context = super(ChoferCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET or None)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            chofer = form.save(commit=False)
            licencia = form2.save()
            licencia.chofer = chofer
            chofer.save()
            licencia.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class ChoferUpdate (UpdateView):
    model = Chofer
    second_model = Licencia
    form_class = ChoferForm
    second_form_class = LicenciaForm
    template_name = 'chofer/chofer_form.html'
    success_url = reverse_lazy('chofer_listar')

    def get_context_data(self, **kwargs):
        context = super(ChoferUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        chofer = self.model.objects.get(cedula=pk)
        licencia = self.second_model.objects.filter(chofer_id=chofer.cedula).first()
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2'not in context:
            context['form2'] = self.second_form_class(instance=licencia)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        pk = kwargs['pk']
        chofer = self.model.objects.get(cedula=pk)
        licencia = self.second_model.objects.filter(chofer_id=chofer.cedula).first()
        form = self.form_class(request.POST, request.FILES or None, instance=chofer)
        form2 = self.second_form_class(request.POST, instance=licencia)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class ChoferDelete (DeleteView):
    model = Chofer
    template_name = 'chofer/chofer_delete.html'
    success_url = reverse_lazy('chofer_listar')


class AsignacionCreate (CreateView):
    model = ChoferVehiculo
    form_class = AsignacionForm
    template_name = 'chofer/choferVehiculo_form.html'
    success_url = reverse_lazy('chofer_listar')

    def form_valid(self, form):
        form.instance.chofer = Chofer.objects.filter(cedula=self.kwargs['pk']).first()
        return super(AsignacionCreate, self).form_valid(form)


class AsignacionDelete(DeleteView):
    model = ChoferVehiculo
    template_name = 'chofer/choferVehiculo_delete.html'
    success_url = reverse_lazy('chofer_listar')


class AsignacionHorarioCreate (CreateView):
    model = ChoferVehiculoHorario
    form_class = AsignacionHorarioForm
    template_name = 'chofer/choferVehiculoHorario_form.html'
    success_url = reverse_lazy('chofer_listar')

    def form_valid(self, form):
        chofer = Chofer.objects.filter(cedula=self.kwargs['pk']).first()
        form.instance.chofer_vehiculo = ChoferVehiculo.objects.filter(chofer=chofer).first()
        return super(AsignacionHorarioCreate, self).form_valid(form)


class AsignacionHorarioUpdate (UpdateView):
    model = ChoferVehiculoHorario
    form_class = AsignacionHorarioForm
    template_name = 'chofer/choferVehiculoHorario_form.html'
    success_url = reverse_lazy('chofer_listar')

