from django import forms
from .models import Darsliklar

class DarsliklarForms(forms.Form):
    class Meta:
        model = Darsliklar
        fields = [
            'image',
            'video',
            'pdf',
            'mavzu',
            'malumotlar'
        ]