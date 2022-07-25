from webbrowser import get
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from neodex.forms import FormularioTrainer
from .models import pokemon, Trainer
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
class FormularioPokemonView(HttpRequest):
    def procesar_formulario_trainer(request):
        poke=pokemon.objects.all()
        if request.method=='POST':
            form=FormularioTrainer(request.POST)
            if form.is_valid():
                print(form)
                form.save()
            return render(request, 'formulario.html', {'form':form, 'pokemon':poke})
        else:
            form=FormularioTrainer()
            return render(request, 'formulario.html', {'form':form, 'pokemon':poke})
    def listar_pokemon(request):
        poke=pokemon.objects.all()
        return render(request, 'ListaPokemon.html',{"pokemon":poke})

    def listar_trainers(request):
        trainers=Trainer.objects.all()
        return render(request, 'trainers.html', {"entrenador":trainers})

    def detalle_pokemon(request, pokemon_id):
        detalle_poke=pokemon.objects.get(id=pokemon_id)
        return render(request, 'PokemonIndex.html', {'detalle':detalle_poke})

    def borrar_trainer(request, id_trainer):
        trainer=Trainer.objects.get(pk=id_trainer)
        trainer.delete()
        trainer=Trainer.objects.all()
        return render(request, "trainers.html", {'entrenador':trainer})
