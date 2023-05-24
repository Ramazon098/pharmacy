from django.urls import path

from knox.views import LogoutView, LogoutAllView

from accounts.views import UsersViewAPI, CreateUserAPI, UpdateUserAPI, LoginUserAPI


# Create your urls here.

urlpatterns = [
    path('users/', UsersViewAPI.as_view()),
    path('create-user/', CreateUserAPI.as_view()),
    path('update-user/<int:pk>/', UpdateUserAPI.as_view()),
    path('login/', LoginUserAPI.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
]
