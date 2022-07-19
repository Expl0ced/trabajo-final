from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import pokemon, Trainer, alto_mando
from django.apps import AppConfig



class NeodexConfig(AppConfig):
    name= 'neodex'


# Register your models here.

admin.site.register(pokemon)
admin.site.register(Trainer)
admin.site.register(alto_mando)