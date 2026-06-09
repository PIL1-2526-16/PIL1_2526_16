from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profil/', views.profil, name='profil'),
    path('profil/modifier/', views.modifier_profil, name='modifier_profil'),
    path('mot-de-passe/reinitialiser/', views.demande_reinitialisation, name='demande_reinitialisation'),
    path('mot-de-passe/nouveau/<uidb64>/<token>/', views.nouveau_mot_de_passe, name='nouveau_mot_de_passe'),
    path('', views.accueil, name = 'accueil'),
]