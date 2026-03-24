from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)

    return Response({'error': 'No account is suitable for this login'}, status=400)


@api_view(['POST'])
def logout_view(request):
    request.user.auth_token.delete()
    return Response({"message": "Wylogowano"}, status=204)

