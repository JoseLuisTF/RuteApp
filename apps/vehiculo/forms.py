from django import forms
from apps.vehiculo.models import Vehiculo


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        labels = {
            'placa': 'Placa',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'anio': 'Año',
            'nPuertas': 'Puertas',
            'capacidad': 'Capacidad',
            'num_motor': 'Numero Motor',
            'num_chasis': 'Numero Chasis',
            'tipo_vehiculo': 'Tipo Vehiculo',
        }
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'nPuertas': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'num_chasis': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_vehiculo': forms.Select(attrs={'class': 'form-control'}),
        }
