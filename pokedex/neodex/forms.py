from django import forms
from .models import pokemon, Trainer

class FormularioTrainer(forms.ModelForm):
    class Meta:
        # first_name=forms.CharField(label="Nombre", max_length=255, min_length=3, required=True)
        # last_name=forms.CharField(label="Apellido", max_length=255, min_length=3, required=True)
        # team=forms.CharField(label="Equipo", max_length=255, min_length=3, required=True)
        # pokemon_1=forms.ModelChoiceField(label="Pokemon 1", queryset=pokemon.objects.all())
        # pokemon_2=forms.ModelChoiceField(label="Pokemon 2", queryset=pokemon.objects.all())
        # pokemon_3=forms.ModelChoiceField(label="Pokemon 3", queryset=pokemon.objects.all())
        # pokemon_4=forms.ModelChoiceField(label="Pokemon 4", queryset=pokemon.objects.all())
        # pokemon_5=forms.ModelChoiceField(label="Pokemon 5", queryset=pokemon.objects.all())
        # pokemon_6=forms.ModelChoiceField(label="Pokemon 6", queryset=pokemon.objects.all())
        model = Trainer
        fields = ['first_name','last_name','team', 'pokemon_1', 'pokemon_2', 'pokemon_3', 'pokemon_4', 'pokemon_5', 'pokemon_6']
        labels= {
            'first_name':'Nombre',
            'last_name':'Apellido',
            'team':'Equipo',
            'pokemon_1':'pokemon 1',
            'pokemon_2':'pokemon 2',
            'pokemon_3':'pokemon 3',
            'pokemon_4':'pokemon 4',
            'pokemon_5':'pokemon 5',
            'pokemon_6':'pokemon 6',    
        }
        widgets={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.TextInput(attrs={'class': 'form-control'}),
            'pokemon_1': forms.TextInput(attrs={'class': 'form-control'}),
            'pokemon_2': forms.TextInput(attrs={'class': 'form-control'}),
            'pokemon_3': forms.TextInput(attrs={'class': 'form-control'}),
            'pokemon_4': forms.TextInput(attrs={'class': 'form-control'}),
            'pokemon_5': forms.TextInput(attrs={'class': 'form-control'}),
            'pokemon_6': forms.TextInput(attrs={'class': 'form-control'})

        }