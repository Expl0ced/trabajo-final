from django import forms
from .models import pokemon, Trainer

class FormularioPokemon(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'