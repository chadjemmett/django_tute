from django import forms

class ItemForm(forms.Form):
    TRANSACTION = [('buy', 'Buy'), ('sell', 'Sell')]
    TYPE = [('herb', 'Herb'), ('scroll', 'Scroll')]
    TYPE = [('herb', 'Herb'), ('scroll', 'Scroll')]
    transaction  = forms.ChoiceField(label="Transaction", choices=TRANSACTION, widget=forms.RadioSelect)
    item_type = forms.ChoiceField(label="Which item?", choices=TYPE, widget=forms.RadioSelect) 
    price = forms.IntegerField(label="Price?")
