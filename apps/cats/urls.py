from django.urls import path
from .views import (
    CatsListApiView, BreedListApiView, CatsApiDetailView, RatingApiDetailView, RateListApiView
)

app_name = 'api'
urlpatterns = [
    path('breedlist/', BreedListApiView.as_view(), name='api_update'),

    path('', CatsListApiView.as_view(),),
    path('<int:pk>/', CatsApiDetailView.as_view()),
    path('<int:pk>/rate/', RatingApiDetailView.as_view(), ),
    path('ratetotal/', RateListApiView.as_view(), ),
]
