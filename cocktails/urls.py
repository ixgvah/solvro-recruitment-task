from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.cocktails_list, name='cocktails'),
    path('users_cocktails/', views.user_cocktails, name='users_cocktails'),
    path('create/', views.create_cocktail, name='create_cocktail'),
    path('users_favourite_cocktails/', views.UsersFavouriteCocktails, name='users_favourite_cocktails'),
    path('<int:pk>/edit/', views.edit_cocktail, name='edit_cocktail'),
    path('<int:pk>/delete/', views.delete_cocktail, name='delete_cocktail'),
]