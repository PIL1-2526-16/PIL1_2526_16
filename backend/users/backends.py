from django.contrib.auth.backends import ModelBackend
from .models import Utilisateur

class EmailOuTelephoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            utilisateur = Utilisateur.objects.get(email=username)
        except Utilisateur.DoesNotExist:
            try:
                utilisateur = Utilisateur.objects.get(telephone=username)
            except Utilisateur.DoesNotExist:
                return None
        
        if utilisateur.check_password(password):
            return utilisateur
        return None