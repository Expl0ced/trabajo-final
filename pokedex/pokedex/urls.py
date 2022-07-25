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
    path('formulario/', FormularioPokemonView.procesar_formulario_trainer, name='formulario'),
    path('ListaPokemon/', FormularioPokemonView.listar_pokemon, name='ListaPokemon'),
    path('ListaPokemon/detalle_pokemon/<int:pokemon_id>', FormularioPokemonView.detalle_pokemon, name='detalle_pokemon'),
    path('trainers/', FormularioPokemonView.listar_trainers, name='trainers'),
    path('trainers/eliminar_trainers/<int:id_trainer>', FormularioPokemonView.borrar_trainer, name='eliminar_trainers')

]
