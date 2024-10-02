from django.urls import path, re_path
from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView,
)

app_name = 'api'
urlpatterns = [
    # path('user/', UserRetrieveUpdateAPIView.as_view(), name='api_update'),
    path('user/register/', RegistrationAPIView.as_view(), name='api_register'),
    path('user/login/', LoginAPIView.as_view(), name='api_login'),
]
