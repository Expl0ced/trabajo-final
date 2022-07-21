"""pokedex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from neodex.HomeVIew import HomeView
from neodex.views import FormularioPokemonView

urlpatterns = [
    # path("neodex/", include('neodex.urls')),  
    path('admin/', admin.site.urls),
    path('',HomeView.home, name='home'),
    path('pagina1/',HomeView.pagina1, name='pagina1'),
    path('pagina2/<int:parametro1>',HomeView.pagina2, name='pagina2'),
    path('formulario/', HomeView.formulario, name='formulario'),
    path('registrarTrainer/', FormularioPokemonView.formulario_trainer, name='registrarTrainer'),
    path('guardartrainer', FormularioPokemonView.procesar_formulario_trainer, name='guardartrainer'),
    path('ListaPokemon/', FormularioPokemonView.listar_pokemon, name='ListaPokemon'),
    # path('ListaPokemon/PokemonIndex/<int:id>',FormularioPokemonView.listar_pokemon, name='PokemonIndex'),
    path('detalle_pokemon/(?P<pokemon_id>\d+)/$', FormularioPokemonView.detalle_pokemon, name='detalle_pokemon'),
    path('trainers/', FormularioPokemonView.listar_trainers, name='trainers')

]
