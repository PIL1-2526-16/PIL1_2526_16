from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('tableau-de-bord/', views.tableau_de_bord, name='tableau_de_bord'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profil/', views.profil, name='profil'),
    path('profil/modifier/', views.modifier_profil, name='modifier_profil'),
    path('profil/competences/', views.gerer_competences, name='gerer_competences'),
    path('profil/mot-de-passe/', views.changer_mot_de_passe, name='changer_mot_de_passe'),
    path('mot-de-passe/reinitialiser/', views.demande_reinitialisation, name='demande_reinitialisation'),
    path('mot-de-passe/nouveau/<uidb64>/<token>/', views.nouveau_mot_de_passe, name='nouveau_mot_de_passe'),
]