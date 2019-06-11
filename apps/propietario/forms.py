from django import forms
from apps.propietario.models import Propietario, PropietarioVehiculo


class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
        labels = {
            'cedula': 'Cedula',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'fecha_nacimiento': 'Fecha Nacimiento',
        }
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
        }


class PropietarioVehiculoForm(forms.ModelForm):
    class Meta:
        model = PropietarioVehiculo
        fields = ['vehiculo', 'fecha_compra']
        labels = {
            'vehiculo': 'Vehiculo',
            'fecha_compra': 'Fecha Compra',
        }
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_compra': forms.DateInput(attrs={'class': 'form-control'}),
        }
