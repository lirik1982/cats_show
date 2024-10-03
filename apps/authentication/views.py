from django.contrib.auth import authenticate, get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from authentication.serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer,
)

User = get_user_model()

class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        User.objects.create_user(**serializer.validated_data)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user is None or not user.is_active:
            return Response({"error": "tut"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"token": user.token}, status=status.HTTP_200_OK)




