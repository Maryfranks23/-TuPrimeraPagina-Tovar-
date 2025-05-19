from django import forms
from .models import Recarga, Cliente, EmpresaRecarga

class EmpresaRecargaForm(forms.ModelForm):
    class Meta:
        model = EmpresaRecarga
        fields = ['nombre']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']

class RecargaForm(forms.ModelForm):
    class Meta:
        model = Recarga
        fields = ['monto', 'telefono', 'empresa', 'cliente']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['monto'].widget = forms.Select(choices=[(500, '$500'), (600, '$600'), (700, '$700'), (800, '$800'), (1000, '$1000')])
        self.fields['empresa'].queryset = EmpresaRecarga.objects.all()
        self.fields['cliente'].queryset = Cliente.objects.all()

class BusquedaRecargaForm(forms.Form):
    telefono = forms.CharField(max_length=10, label='Buscar Recarga por Teléfono')