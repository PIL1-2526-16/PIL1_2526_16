from django.urls import path
from . import views

app_name = 'messaging' 

urlpatterns = [
    path('', views.liste_conversations, name='liste_conversations'),
    path('<int:id_conversation>/', views.detail_conversation, name='detail_conversation'),
    path('demarrer/<int:id_utilisateur>/', views.demarrer_conversation, name='demarrer_conversation'),
    path('<int:id_conversation>/nouveaux/', views.nouveaux_messages, name='nouveaux_messages'),
]