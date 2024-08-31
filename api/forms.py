from django.forms import ModelForm
from api.models import Food
from django import forms

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ('name','date','number')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }