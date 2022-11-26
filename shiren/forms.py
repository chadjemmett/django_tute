from django import forms
from bootstrap5.widgets import RadioSelectButtonGroup
from .models import Item

class ItemForm(forms.Form):
    TRANSACTION = [
            ('buy', 'buy'), 
            ('sell', 'sell')
            ]
    TYPE = [
            (10,'herb'), 
            (20, 'scroll'), 
            (30, 'staff'), 
            (40, 'jar'), 
            (50, 'bracelet'),
            ]

    transaction  = forms.ChoiceField(
            label="Transaction", 
            choices=TRANSACTION, 
            widget=RadioSelectButtonGroup
            )
    
    
    item_type = forms.ChoiceField(
            label="Which item?", 
            choices=TYPE, 
            widget=RadioSelectButtonGroup) 

    price = forms.IntegerField()

class ListForm(forms.Form):
    checkbox_thing = forms.BooleanField(required=False, widget=forms.CheckboxInput())

