from rest_framework import serializers
from .models import CatBreed, Cat, Rating
from api.serializers import UserSerializer


class CatBreedkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatBreed
        fields = ('id', 'name')


class CatSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Cat
        fields = ('id', 'name', 'age', 'breed', 'owner', 'color', 'description')


class RateSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    cat = CatSerializer()

    class Meta:
        model = Rating
        fields = ('id', 'cat', 'average_rate')

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['date_since_taked'] = (timezone.now() - instance.date_taken).days
    #     representation.pop('date_get_back')
    #     return representation
