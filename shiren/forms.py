from django import forms
from bootstrap5.widgets import RadioSelectButtonGroup

class ItemForm(forms.Form):
    TRANSACTION = [('buy', 'Buy'), ('sell', 'Sell')]
    TYPE = [('herb', 'Herb'), ('scroll', 'Scroll'), ('wand', 'Wand'), ('jar', 'Jar'), ('armband', 'Armband')]
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
