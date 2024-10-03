from rest_framework import serializers
from django.contrib.auth import authenticate

from authentication.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token',)
        read_only_fields = ('token',)
