from webbrowser import get
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from neodex.forms import FormularioPokemon
from .models import pokemon, Trainer

# Create your views here.

def index(request):
    pass 

class HomeView():

    def home(self):
        plantilla=get_template('index.html')
        return(HttpResponse(plantilla.render()))

    def nosexd(request):
        poke=pokemon.objects.all()
        return render(request, 'aaaaa.html', {"pokemon":poke})

class FormularioPokemonView(HttpRequest):
    def index(request):
        poke = FormularioPokemon()
        return render(request, "PokemonIndex.html", {"form":poke})


    def procesar_formulario(request):
        poke=FormularioPokemon()
        if poke.is_valid():
            poke.save()
            poke=FormularioPokemon()
        return render(request, "PokemonIndex.html", {"form":poke, "mensaje":'ok'})

    def formulario_trainer(request):
        trainer=FormularioPokemon()
        return render(request, 'formulario.html', {"formulario":trainer})

    def procesar_formulario_trainer(request):
        trainer=(FormularioPokemon())
        if trainer.is_valid():
            trainer.save()
            trainer=FormularioPokemon()
        return render(request, 'formulario.html', {"formulario":trainer, "mensaje":'ok'})

    def listar_pokemon(request):
        poke=pokemon.objects.all()
        return render(request, 'ListaPokemon.html',{"pokemon":poke})

    def listar_trainers(request):
        trainers=Trainer.objects.all()
        return render(request, 'trainers.html', {"entrenador":trainers})

    def detalle_pokemon(request, pokemon_id):
        detalle_poke=pokemon.objects.get(id=pokemon_id)
        return render(request, 'PokemonIndex.html', {'pokemon':detalle_poke})