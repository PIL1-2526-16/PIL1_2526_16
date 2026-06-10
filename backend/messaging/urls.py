from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.conversations, name='conversations'),
    path('demarrer/<int:utilisateur_id>/', views.demarrer_conversation, name='demarrer_conversation'),
    path('<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
]
