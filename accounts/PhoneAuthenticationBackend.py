from django.contrib.auth.models import User


class PhoneBackend(object):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(profile__phone=username)
        except User.MultipleObjectsReturned:
            user = User.objects.filter(
                profile__phone=username).order_by('id').first()
        except User.DoesNotExist:
            return None

        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
