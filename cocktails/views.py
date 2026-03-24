from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cocktail, UsersFavouriteCocktails, Ingredient
from .serializers import CocktailSerializer, IngredientSerializer


class CocktailList(generics.ListCreateAPIView):
    serializer_class = CocktailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #zalogowany moze wykonac POST, niezalogowany tylko odczyt

    def get_queryset(self):
        queryset = Cocktail.objects.all()
        filter = self.request.query_params.get('filter')

        if filter == 'mine' and self.request.user.is_authenticated: #zabezpieczenie
            return queryset.filter(user=self.request.user)

        if filter == 'fav' and self.request.user.is_authenticated:
            return queryset.filter(favorited_by__user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CocktailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IngredientList(generics.ListCreateAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Ingredient.objects.all()

        return queryset

    def perform_create(self, serializer):
        serializer.save() #tym razem bez user=self.request.user bo nie przy[isujemy autora do skladnika


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

