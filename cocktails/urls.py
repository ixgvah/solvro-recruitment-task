from django.urls import path
from .views import CocktailList, CocktailDetail, IngredientList, IngredientDetail

urlpatterns = [
    path('cocktails/', CocktailList.as_view(), name='cocktail-list'),
    path('cocktails/<int:pk>/', CocktailDetail.as_view(), name='cocktail-detail'),
    path('ingredients/', IngredientList.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', IngredientDetail.as_view(), name='ingredient-detail'),
]