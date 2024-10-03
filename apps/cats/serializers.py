from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CatBreed, Cat, Rating
from authentication.serializers import UserSerializer

User = get_user_model()

class CatBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatBreed
        fields = ('id', 'name')


class CatSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    average_rate = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=6)
    rate_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Cat
        fields = ('id', 'name', 'age', 'breed', 'owner', 'color', 'description', 'average_rate', 'rate_count')


class CatListSerializer(serializers.ModelSerializer):
    average_rate = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=6)
    rate_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Cat
        fields = ('id', 'name', 'owner', 'breed', 'color', 'average_rate', 'rate_count')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('rating', )

