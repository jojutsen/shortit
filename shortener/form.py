from dataclasses import field, fields
from django import forms
from .models import UrlsDatabase

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlsDatabase
        fields={
            'url',
        }