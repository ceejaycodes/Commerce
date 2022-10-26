from decimal import Decimal
from django.forms import CheckboxInput, CheckboxSelectMultiple, DecimalField, ModelChoiceField, ModelForm, MultipleChoiceField, MultipleHiddenInput, NumberInput, TextInput, Textarea, URLInput
from sqlalchemy import false

from .models import User, AuctionListing, Bid, Comment



class Auctionform(ModelForm):
    
    class Meta:
        model = AuctionListing
        fields = ['item','description','image','category']
        exclude = ['listed_by','bid']
        widgets = {
            'item': TextInput(attrs={
                'class': "form-control",
                'style': 'margin: 0.4rem;',
                'placeholder': 'Name',
                'required': 'True'
                }),
            'description': Textarea(attrs={
                'class': "form-control",
                'style':  'margin: 0.4rem; word-wrap:inherit; resize: none;',
                'placeholder': 'Description',
                'required': 'True'
                }),
            'image': URLInput(attrs={
                'class': "form-control",
                'style':  'margin: 0.4rem;',
                'placeholder': 'input image URL',
                'required': 'True'
                })
        }

class Bidform(ModelForm):
    
    
    class Meta:
        model = Bid
        fields = ['price']
        exclude = ['bid_by']
        widgets = {
            'price' : NumberInput(attrs={
                'class': 'form-control',
                'style': 'margin: 0.4rem',
                'placeholder': 'place bid',
                'min':0,
                'required': 'True'
            })
        }
        labels = {
            'price': ('Bid'),
            }
        
    

class Commentform(ModelForm):
    
    
    
    class Meta:
        model = Comment
        fields = ['comment']
        exclude = ['author','item']
        widgets = {
            'comment' : Textarea(attrs={
            'class': 'form-control',
            'style': 'margin: 0.4rem; resize: none;',
            'placeholder': 'Please Leave A Review'
            })
        }