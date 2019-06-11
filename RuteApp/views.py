from django.views.generic import TemplateView

from apps.chofer.models import Chofer
from apps.propietario.models import Propietario
from apps.ruta.models import Ruta
from apps.vehiculo.models import Vehiculo


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['cantidades'] = {
            'choferes': Chofer.objects.all().count(),
            'propietarios': Propietario.objects.all().count(),
            'vehiculos': Vehiculo.objects.all().count(),
            'rutas': Ruta.objects.all().count(),
        }
        return context
