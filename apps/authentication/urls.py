from django.urls import path, re_path
from .views import (
    LoginAPIView, RegistrationAPIView,
)

app_name = 'api'
urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='api_register'),
    path('login/', LoginAPIView.as_view(), name='api_login'),
]
