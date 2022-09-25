from django.urls import  path

from .views import *
from . import views

urlpatterns = [ 
    path('monitores/<int:id>', views.monitorView, name='monitor_view'),
    path('monitores/telas', views.monitorList, name='monitor_list'),
    path('monitores/add-monitor', views.newMonitor, name='new_monitor'),
    path('monitores/edit/<int:id>', views.editMonitor, name='edit_monitor'),
]