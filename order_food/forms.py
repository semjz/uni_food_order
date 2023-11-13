from django import forms
from django.forms import modelformset_factory, formset_factory

from .models import Food


class OrderForm(forms.Form):
    foods = forms.ModelChoiceField(queryset=Food.objects.all(), widget=forms.Select(attrs={'class': 'food-select'}),
                                   empty_label=None)
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'quantity-input'}))
