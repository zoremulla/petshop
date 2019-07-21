from django import forms
from .models import pets

class Petsform(forms.ModelForm):
    class Meta:
        model = pets
        fields = '__all__'

     
