from django import forms
from reserva_APP.models import reserva

class FormReserva(forms.ModelForm):
    
    nombre = forms.CharField(label='Nombre', min_length=5, max_length=20)
    telefono = forms.CharField(min_length=9, max_length=9)
    numeroPersonas = forms.IntegerField(label='Cantidad de Personas', min_value=1, max_value=15)
    observacion = forms.CharField(required=False)
    estados = [('completada', 'COMPLETADA'),('reservado', 'RESERVADO'),('anulada', 'ANULADA'),('no asisten', 'NO ASISTEN')] 
    estado = forms.CharField(widget=forms.Select(choices=estados))
    class Meta:
        model = reserva
        fields = '__all__'

    