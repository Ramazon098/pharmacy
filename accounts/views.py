from django.contrib.auth import login, logout

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from knox.views import LoginView

from accounts.models import CustomUser
from accounts.serializers import (
    UserSerializer,
    CreateUserSerializer,
    UpdateUserSerializer,
    LoginUserSerializer,
)


# Create your views here.

class UsersViewAPI(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]


class CreateUserAPI(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny,]


class UpdateUserAPI(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated,]


class LoginUserAPI(LoginView):
    permission_classes = [AllowAny,]
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
