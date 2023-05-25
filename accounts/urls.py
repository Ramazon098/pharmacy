from django.urls import path

from accounts.views import UsersViewAPI, CreateUserAPI, UpdateUserAPI, LoginUserAPI, LogoutAPI


# Create your urls here.

urlpatterns = [
    path('users/', UsersViewAPI.as_view()),
    path('create-user/', CreateUserAPI.as_view()),
    path('update-user/<int:pk>/', UpdateUserAPI.as_view()),
    path('login/', LoginUserAPI.as_view()),
    path('logout/', LogoutAPI.as_view()),
]
