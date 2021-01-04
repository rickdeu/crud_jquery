from django.contrib import admin
from core.models import *

class AlvoAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Alvo', {'fields': ['nome_alvo','data_expiracao',]}),
        ('Localização', {'fields':['lat', 'lon'], }),
       
    ]


    list_display=['id','nome_alvo', 'lat', 'lon', 'data_expiracao']
    list_display_links=['id','nome_alvo', 'lat', 'lon', 'data_expiracao']
    save_on_top=True



admin.site.register(Alvo, AlvoAdmin)