from django.urls import path
from . import views

app_name = 'matching'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('proposer/<int:utilisateur_id>/', views.proposer, name='proposer'),
    path('accepter/<int:matching_id>/', views.accepter, name='accepter'),
    path('refuser/<int:matching_id>/', views.refuser, name='refuser'),
]
