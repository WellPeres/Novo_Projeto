from django.contrib import admin
from .models import Monitor

# Register your models here.

class ListaMonitor(admin.ModelAdmin):
    list_display = ('id', 'monitor', 'modelo','service_tag', 'polegadas', )
    search_fields = ('monitor', 'modelo','service_tag', 'polegadas',)
    list_display_links = ('modelo',)

    list_display2 = ('id', 'monitor', 'modelo','service_tag', 'polegadas', )
    search_fields2 = ('monitor', 'modelo','service_tag', 'polegadas',)
    list_display_links2 = ('modelo',)

admin.site.register(Monitor, ListaMonitor)


