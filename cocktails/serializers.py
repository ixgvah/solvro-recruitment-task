from rest_framework import serializers
from .models import Cocktail, Ingredient, CocktailIngredients

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'      #wszystkie pola zamien ja JSON

class CocktailIngredientsSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name') #pokaze to oprocz samwgo id

    class Meta:
        model = CocktailIngredients
        fields = ['ingredient', 'ingredient_name', 'quantity', 'unit'] #na JSON zamien te pola

class CocktailSerializer(serializers.ModelSerializer):
    recipe = CocktailIngredientsSerializer(source='recipe_ingredients', many=True)
    author = serializers.ReadOnlyField(source='user.username')  #POKAZE NAZWE ZAMIAST ID

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'category', 'author', 'recipe', 'image']

    def create(self, validated_data):
        ingredients = validated_data.pop('recipe_ingredients', None)

        cocktail = Cocktail.objects.create(**validated_data)

        for ingredient in ingredients:
            CocktailIngredients.objects.create(cocktail=cocktail, **ingredient)
        return cocktail

    def update(self, instance, validated_data):
        recipe_data = validated_data.pop('recipe_ingredients', None)
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)

        if 'image' in validated_data:
            instance.image = validated_data.get('image', instance.image)
        instance.save()

        if recipe_data is not None:
            instance.recipe_ingredients.all().delete()
            for item in recipe_data:
                CocktailIngredients.objects.create(cocktail=instance, **item)

        return instance