from webbrowser import get
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from pokedex.neodex.forms import FormularioPokemon
from .models import pokemon

# Create your views here.

def index(request):
    pass 

class HomeView():

    def home(self):
        plantilla=get_template('index.html')
        return(HttpResponse(plantilla.render()))




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

    def listar_pokemon(request):
        poke=pokemon.objects.all()
        return render(request, 'ListaPokemon.html',{"pokemon":poke})