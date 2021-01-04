from django import forms
#from django.forms import ModelForm
from core.models import * 

#Reutilizacao da entidade para criacao do formulario
class AlvoForm(forms.ModelForm):
    nome_alvo = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'text','class': 'form-control'}
        ),
        max_length=30, 
        required=True, 
        help_text='Informe o nome',
        label='Nome'
        )
    lat = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'text','class': 'form-control'}
        ),
        max_length=30, 
        required=True, 
        help_text='Informe a latitude',
        label='Latitude'
        )
    lon = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'text','class': 'form-control'}
        ),
        max_length=30, 
        required=True, 
        help_text='Informe a longitude',
        label='Longitude'
        )
    data_expiracao = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date','class': 'form-control'}
        ), 
        required=True, 
        help_text='Informe a data de expiração',
        label='Data de expiração'
        )
    class Meta:
        model=Alvo
        fields = '__all__'

