from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request):
    return Response({
        'cocktails': reverse('cocktail-list', request=request),
        'ingredients': reverse('ingredient-list', request=request),
        'users': reverse('user-list', request=request),
    })