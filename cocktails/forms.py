from django import forms
from .models import Cocktail, Ingredient, CocktailIngrediets
from django.forms import inlineformset_factory

class CocktailForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = ['name', 'category', 'description', 'image']




CocktailIngredientFormSet = inlineformset_factory(
    Cocktail,
    CocktailIngrediets,
    fields=['ingredient', 'quantity', 'unit'],
    extra=5,
    can_delete=True,
)

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'description', 'image', 'is_alcoholic']