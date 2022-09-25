from dataclasses import fields
from django import forms

from .models import Monitor

class MonitorForm(forms.ModelForm):

    class Meta:
        model = Monitor
        fields = ('monitor', 'modelo','service_tag', 'polegadas', 'monitor2', 'modelo2', 'service_tag2', 'polegadas2')