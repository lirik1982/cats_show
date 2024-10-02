from django.db import IntegrityError
from django.db.models import Avg
from rest_framework import status, generics
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cats.models import CatBreed, Cat, Rating
from .serializers import CatBreedkSerializer, CatSerializer, RateSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BreedListApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CatBreed.objects.all()
    serializer_class = CatBreedkSerializer


class AddCatBreed(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        breed_name = request.data['name']
        try:
            new_breed = CatBreed(name=breed_name)
            new_breed.save()
        except IntegrityError:
            return Response({'Операция': 'Неудача', "info": "Уже имеется в бд"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Операция': 'Неудача'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Операция': 'Успешно', 'id': new_breed.id}, status=status.HTTP_200_OK)


class CatsListApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['breed', 'id']


class CatsApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CatSerializer

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        if Cat.objects.filter(
                name=request.data['name'],
                owner=request.user
        ).exists():
            return Response(
                {'Операция': 'Неудача', "info": "Питомец с такими кличкой и хозяиным уже введен"},
                status=status.HTTP_400_BAD_REQUEST
            )

        breed = CatBreed.objects.get(id=request.data['breed_id'])
        try:
            cat = Cat(
                name=request.data['name'],
                owner=request.user,
                breed=breed,
                color=request.data['color'],
                age=request.data['age'],
                description=request.data['description'],
            )
            cat.save()
        except Exception as e:
            return Response({'Операция': 'Неудача'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Операция': 'Успешно', 'id': cat.id}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        cat = self.get_object()
        serializer = self.get_serializer(cat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        cat_id = self.kwargs['pk']
        cat = get_object_or_404(Cat, pk=cat_id)
        cat.delete()
        return Response({'status': 'deleted'}, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        data = request.data
        cat = get_object_or_404(Cat, id=self.kwargs['pk'])
        serializer = CatSerializer(data=data, instance=cat, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "ok"},status=status.HTTP_200_OK)


class RatingApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RateSerializer

    def post(self, request, *args, **kwargs):
        cat = Cat.objects.get(pk=request.data['cat_id'])
        if cat.owner == self.request.user:
            return Response(
                {'Операция': 'Неудача', "info": "Нельзя оценивать своих кошек"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if Rating.objects.filter(cat=cat, user=self.request.user).exists():
            return Response(
                {'Операция': 'Неудача', "info": "Вы уже оценили эту кошку"},
                status=status.HTTP_400_BAD_REQUEST
            )

        rate = Rating.objects.create(
            cat=cat,
            user=self.request.user,
            rating=request.data['rate'],
        )
        rate.save()
        return Response({'Операция': 'Успешно', 'id': rate.id}, status=status.HTTP_200_OK)


class RateListApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = Rating.objects.all()
    queryset = Rating.objects.annotate(
        average_rate=Avg('rating')
    ).order_by('-average_rate')

    serializer_class = RateSerializer
    filter_backends = [DjangoFilterBackend]
