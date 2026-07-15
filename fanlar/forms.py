from django import forms
from .models import Fanlar

class FanlarForms(forms.ModelForm):
    class Meta:
        model = Fanlar
        fields = '__all__'
