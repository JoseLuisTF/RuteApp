from django import forms
from apps.chofer.models import Chofer, Licencia, ChoferVehiculo, ChoferVehiculoHorario


class ChoferForm (forms.ModelForm):
        class Meta:
            model = Chofer
            fields = '__all__'
            labels = {
                'cedula': 'Cedula',
                'nombre': 'Nombre',
                'apellido': 'Apellido',
                'fecha_nacimiento': 'Fecha de Nacimiento',
                'tipo_chofer': 'Tipo de Chofer',
            }
            widgets = {
                'cedula': forms.TextInput(attrs={'class': 'form-control'}),
                'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'apellido': forms.TextInput(attrs={'class': 'form-control'}),
                'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control date-inputmask'}),
                'tipo_chofer': forms.Select(attrs={'class': 'form-control'}),
            }


class LicenciaForm(forms.ModelForm):
    class Meta:
        model = Licencia
        fields = [
            'num_licencia',
            'categoria',
            'fec_expedicion',
            'fec_vencimiento',
            'oficia_expedida',
        ]
        labels = {
            'num_licencia': 'Licencia',
            'categoria': 'Categoria',
            'fec_expedicion': 'Fecha de Expedicion',
            'fec_vencimiento': 'Fecha de Vencimiento',
            'oficia_expedida': 'Oficina Expedicion',
        }
        widgets = {
            'num_licencia': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'fec_expedicion': forms.DateInput(attrs={'class': 'form-control date-inputmask'}),
            'fec_vencimiento': forms.DateInput(attrs={'class': 'form-control date-inputmask'}),
            'oficia_expedida': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AsignacionForm(forms.ModelForm):
    class Meta:
        model = ChoferVehiculo
        fields = [
            'vehiculo',
            'fecha_asignacion',
        ]
        labels = {
            'vehiculo': 'Vehiculo',
            'fecha_asignacion': 'Fecha de Asignacion',
        }
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_asignacion': forms.DateInput(attrs={'class': 'form-control date-inputmask'}),
        }


class AsignacionHorarioForm(forms.ModelForm):
    class Meta:
        model = ChoferVehiculoHorario
        fields = [
            'horario_turno',
        ]
        labels = {
            'horario_turno': 'Tipo de Horario',
        }
        widgets = {
            'horario_turno': forms.Select(attrs={'class': 'form-control'}),
        }
