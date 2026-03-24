from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        #valid_data - dane uzytkownika
        #create vs create_user - create_user zapisuje jako tekst, create hashuje haslo
        user = User.objects.create_user(**validated_data)
        return user