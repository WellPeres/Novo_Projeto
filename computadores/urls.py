from django.urls import  path

from .views import *
from . import views

urlpatterns = [ 
    path('computadores/<int:id>', views.maquinasView, name='maquinas_view'),
    path('computadores/maquinas', views.maquinasList, name='maquinas_list'),
    path('computadores/add-computador', views.newComputador, name='new_computador'),
    path('computadores/edit/<int:id>', views.editComputador, name='edit_computador'),
]