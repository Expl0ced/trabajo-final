from django import forms
from .models import pokemon

class FormularioPokemon(forms.ModelForm):
    class Meta:
        model = pokemon
        fields = '__all__'
        widgets = {'Peso': forms.FloatField(attrs={'type':'float'})}