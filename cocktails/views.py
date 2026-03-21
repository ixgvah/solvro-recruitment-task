from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cocktail, UsersFavouriteCocktails
from .forms import CocktailForm


def cocktails_list(request):
    cocktails = Cocktail.objects.all()
    return render(request, 'cocktails/cocktails_list.html', {'cocktails':cocktails})

def user_cocktails(request):
    cocktails = request.user.cocktails.all()
    return render(request, 'cocktails/user_cocktails.html', {'user': request.user, 'cocktails':cocktails})

@login_required
def create_cocktail(request):
    if request.method == 'POST':
        form = CocktailForm(request.POST, request.FILES)
        if form.is_valid():
            cocktail = form.save(commit=False)
            cocktail.user = request.user
            cocktail.save()
            return redirect('/cocktails/')
    else:
        form = CocktailForm()
    return render(request, 'cocktails/create_cocktail.html', {'form': form})

@login_required
def edit_cocktail(request, pk):
    cocktail = get_object_or_404(Cocktail, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CocktailForm(request.POST, request.FILES, instance=cocktail)
        if form.is_valid():
            form.save()
            return redirect('/cocktails/users_cocktails/')
    else:
        form = CocktailForm(instance=cocktail)
    return render(request, 'cocktails/edit_cocktail.html', {'form': form})

@login_required
def delete_cocktail(request, pk):
    cocktail = get_object_or_404(Cocktail, pk=pk, user=request.user)
    if request.method == 'POST':
        cocktail.delete()
        return redirect('/cocktails/')

@login_required
def starred_cocktails(request):
    favourites = UsersFavouriteCocktails.objects.filter(user=request.user).values_list('cocktail', flat=True)
    cocktails = Cocktail.objects.filter(id__in=favourites)
    return render(request, 'cocktails/user_favourite_cocktails.html', {'cocktails': cocktails})

@login_required
def add_favourite(request, pk):
    cocktail = get_object_or_404(Cocktail, pk=pk)
    UsersFavouriteCocktails.objects.get_or_create(user=request.user, cocktail=cocktail)
    return redirect('/cocktails/')

@login_required
def remove_favourite(request, pk):
    UsersFavouriteCocktails.objects.filter(user=request.user, cocktail__pk=pk).delete()
    return redirect('/cocktails/')