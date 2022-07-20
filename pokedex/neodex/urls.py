from django.urls import URLPattern, path

from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('trainers/', views.listar_trainers, name='trainers')
]