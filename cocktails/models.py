from django.db import models
from django.conf import settings

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    is_alcoholic = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null = True, blank=True)

    def __str__(self):
        return self.name

class Cocktail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cocktails', null=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient, through='CocktailIngredients', related_name='used_in')
    image = models.ImageField(upload_to='cocktails/', null = True, blank=True)

    def __str__(self):
        return self.name

class CocktailIngredients(models.Model):
    # 'recipe_ingredients' to klucz do sukcesu w Serializerze!
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    unit = models.CharField(max_length=10, default='ml')

class UsersFavouriteCocktails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'cocktail')