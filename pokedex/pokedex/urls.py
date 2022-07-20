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
    path('pagina3/<int:parametro1>/<int:parametro2>',HomeView.pagina3, name='pagina3'),
    path('formulario/', HomeView.formulario, name='formulario'),
    path('ListaPokemon/', HomeView.listapoke, name='ListaPokemon'),
    path('prototipo/', HomeView.nosexd, name='prototipo'),
    path('trainers/', FormularioPokemonView, name='trainers')

]
