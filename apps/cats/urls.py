from django.urls import path
from .views import (
    CatsListApiView, AddCatBreed, BreedListApiView, CatsApiDetailView, RatingApiDetailView, RateListApiView
)

app_name = 'api'
urlpatterns = [
    path('addbreed/', AddCatBreed.as_view(), name='api_update'),
    path('breedlist/', BreedListApiView.as_view(), name='api_update'),

    path('addcat/', CatsApiDetailView.as_view(),),
    path('detail/<int:pk>/', CatsApiDetailView.as_view()),
    path('list/', CatsListApiView.as_view(),),

    path('rate/', RatingApiDetailView.as_view(), ),
    path('ratetotal/', RateListApiView.as_view(), ),
]
