from rest_framework import serializers

from accounts.models import CustomUser


# Create your serializers here.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name']
