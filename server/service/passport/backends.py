from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class PassportBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        user_model = get_user_model()

        try:
            user = user_model.objects.get(username=username)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            return None

    def get_user(self, user_id):
        user_model = get_user_model()

        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
