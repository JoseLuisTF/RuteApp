from django import forms
from apps.ruta.models import Punto, Ruta, PuntoRuta, RutaAsignada


class PuntoForm(forms.ModelForm):
    class Meta:
        model = Punto
        fields = ['nom_punto']
        labels = {
            'nom_punto': 'Nombre del Punto',
        }
        widgets = {
            'nom_punto': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['descripcion_ruta', 'resolucion']
        labels = {
            'descripcion_ruta': 'Descripcion de la Ruta',
            'resolucion': 'Numero Resolucion',
        }
        widgets = {
            'descripcion_ruta': forms.TextInput(attrs={'class': 'form-control'}),
            'resolucion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PuntoRutaForm(forms.ModelForm):
    class Meta:
        model = PuntoRuta
        fields = ['tipo_punto', 'punto']
        labels = {
            'tipo_punto': 'Tipo de Punto',
            'punto': 'Punto',
        }
        widgets = {
            'tipo_punto': forms.Select(attrs={'class': 'form-control'}),
            'punto': forms.Select(attrs={'class': 'form-control'}),
        }


class RutaAsignadaForm(forms.ModelForm):
    class Meta:
        model = RutaAsignada
        fields = ['chofer_vehiculo']
        labels = {
            'chofer_vehiculo': 'Chofer Vehiculo',
        }
        widgets = {
            'chofer_vehiculo': forms.Select(attrs={'class': 'form-control'}),
        }
