from django.urls import  path

from .views import *
from . import views

urlpatterns = [ 
    path('usuarios/<int:id>', views.usuarioView, name='usuario_view'),
    path('usuarios/user', views.usuarioList, name='usuario_list'),
    path('usuarios/add-usuario', views.newUsuario, name='new_usuario'),
    path('usuarios/edit/<int:id>', views.editUsuario, name='edit_usuario'),
]