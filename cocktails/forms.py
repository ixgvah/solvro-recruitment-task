from django import forms
from .models import Cocktail, Ingredient, CocktailIngrediets

class CocktailForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = ['name', 'category', 'description', 'image']