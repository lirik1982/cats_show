from django.db import IntegrityError
from django.db.models import Avg, Count
from rest_framework import status, generics
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, get_object_or_404, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response

from cats.models import CatBreed, Cat, Rating
from .serializers import CatBreedSerializer, CatSerializer, RateSerializer, CatListSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BreedListApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CatBreed.objects.all()
    serializer_class = CatBreedSerializer


class CatsListApiView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Cat.objects.all().annotate(
        average_rate=Avg('rating__rating'),
        rate_count=Count('rating'),
    )
    serializer_class = CatListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['breed', 'owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CatsApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CatSerializer
    queryset = Cat.objects.all().annotate(
        average_rate=Avg('rating__rating'),
        rate_count=Count('rating'),
    )

    def has_object_permission(self, request, view, obj):
        return self.request.user == obj.owner


class RatingPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user == view.cat.owner:
            return None
        return not Rating.objects.filter(user=request.user, cat=view.cat).exists()


class RatingApiDetailView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, RatingPermissions)
    serializer_class = RateSerializer


    @property
    def cat(self):
        return Cat.objects.get(pk=self.kwargs['pk'])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, cat=self.cat)


class RateListApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Rating.objects.annotate(
        average_rate=Avg('rating')
    ).order_by('-average_rate')

    serializer_class = RateSerializer
    filter_backends = [DjangoFilterBackend]
