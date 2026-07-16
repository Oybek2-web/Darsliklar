from django import forms
from .models import Darsliklar

class DarsliklarForms(forms.ModelForm):
    class Meta:
        model = Darsliklar
        fields = '__all__'