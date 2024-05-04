from dal import autocomplete
from .models import Events, Client
from django import forms
from django.urls import reverse_lazy


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
        widgets = {
            'name': autocomplete.ListSelect2(url='client-autocomplete'),
        }