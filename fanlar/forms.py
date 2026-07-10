from django import forms
from .models import Fanlar

class FanlarForms(forms.Form):
    class Meta:
        model = Fanlar
        fields = [
            'title'
        ]