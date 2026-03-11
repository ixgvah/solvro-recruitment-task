from django.shortcuts import render
from .models import Cocktail
def cocktails_list(request):
    cocktails = Cocktail.objects.all()
    return render(request, 'cocktails/cocktails_list.html', {'cocktails':cocktails})
