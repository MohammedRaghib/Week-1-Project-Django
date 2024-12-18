from .models import foods
from django import forms

class foodform(forms.ModelForm):
    class meta:
        model = foods
        fields = ['Name', 'Amount of calories']