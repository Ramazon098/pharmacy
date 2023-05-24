from django.contrib.auth import login

from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from knox.views import LoginView

from accounts.models import CustomUser
from accounts.serializers import UserSerializer, CreateUserSerializer, UpdateUserSerializer, LoginUserSerializer


# Create your views here.

class UsersViewAPI(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class CreateUserAPI(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny,]


class UpdateUserAPI(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer


class LoginUserAPI(LoginView):
    permission_classes = [AllowAny,]
    serializer_class = LoginUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response.data, status=status.HTTP_200_OK)
