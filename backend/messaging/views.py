from django.db import models as db_models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from django.contrib.auth import get_user_model
from .models import Conversation, Message

Utilisateur = get_user_model()


@login_required
def conversations(request):
    qs = Conversation.objects.filter(
        db_models.Q(utilisateur1=request.user) | db_models.Q(utilisateur2=request.user)
    ).order_by('-date_creation')

    liste = []
    for conv in qs:
        autre = conv.autre_participant(request.user)
        dernier_message = conv.messages.last()
        non_lus = conv.messages.filter(lu=False).exclude(expediteur=request.user).count()
        liste.append({
            'conversation': conv,
            'autre': autre,
            'dernier_message': dernier_message,
            'non_lus': non_lus,
        })

    return render(request, 'messaging/conversations.html', {'conversations': liste})


@login_required
def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(
        Conversation.objects.filter(
            db_models.Q(utilisateur1=request.user) | db_models.Q(utilisateur2=request.user)
        ),
        id=conversation_id
    )
    autre = conversation.autre_participant(request.user)

    if request.method == 'POST':
        contenu = request.POST.get('contenu', '').strip()
        fichier = request.FILES.get('fichier')
        if contenu or fichier:
            Message.objects.create(conversation=conversation, expediteur=request.user, contenu=contenu, fichier=fichier)
        return redirect('messaging:conversation_detail', conversation_id=conversation.id)

    conversation.messages.exclude(expediteur=request.user).update(lu=True)

    return render(request, 'messaging/conversation_detail.html', {
        'conversation': conversation,
        'autre': autre,
        'messages_chat': conversation.messages.all(),
    })


@login_required
def demarrer_conversation(request, utilisateur_id):
    autre = get_object_or_404(Utilisateur, id=utilisateur_id)
    if autre == request.user:
        django_messages.error(request, "Vous ne pouvez pas discuter avec vous-même.")
        return redirect('matching:liste')

    conversation = Conversation.objects.filter(
        db_models.Q(utilisateur1=request.user, utilisateur2=autre) |
        db_models.Q(utilisateur1=autre, utilisateur2=request.user)
    ).first()

    if not conversation:
        conversation = Conversation.objects.create(utilisateur1=request.user, utilisateur2=autre)

    return redirect('messaging:conversation_detail', conversation_id=conversation.id)
