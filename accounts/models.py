from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email
