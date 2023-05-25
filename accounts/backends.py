from django.contrib.auth.backends import ModelBackend

from accounts.models import CustomUser


# Create your backends here.

class EmailModelBackend(ModelBackend):
    def authenticate(self, request, email, password):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user

        except CustomUser.DoesNotExist:
            return None
        
        return None
