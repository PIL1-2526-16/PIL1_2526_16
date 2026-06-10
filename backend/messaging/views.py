from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q, Max, OuterRef, Subquery
from django.utils import timezone
from .models import Conversation, Message
from .forms import MessageForm


def get_or_create_conversation(user1, user2):
    """
    Récupère une conversation existante entre deux utilisateurs,
    ou en crée une nouvelle si elle n'existe pas encore.
    On cherche dans les deux sens (user1/user2 ou user2/user1).
    """
    conversation = Conversation.objects.filter(
        Q(id_utilisateur1=user1, id_utilisateur2=user2) |
        Q(id_utilisateur1=user2, id_utilisateur2=user1)
    ).first()

    if not conversation:
        conversation = Conversation.objects.create(
            id_utilisateur1=user1,
            id_utilisateur2=user2
        )
    return conversation


@login_required  # Redirige vers la page de connexion si l'utilisateur n'est pas connecté
def liste_conversations(request):
    """
    Affiche la liste de toutes les conversations de l'utilisateur connecté,
    triées par date du dernier message (la plus récente en premier).
    """
    user = request.user

    # Récupère toutes les conversations où l'utilisateur est participant
    conversations = Conversation.objects.filter(
        Q(id_utilisateur1=user) | Q(id_utilisateur2=user)
    )

    # Pour chaque conversation, on prépare les infos à afficher
    conversations_data = []
    for conv in conversations:
        other_user = conv.get_other_participant(user)
        last_message = conv.messages.order_by('-date_envoi').first()
        unread_count = conv.messages.filter(lu=False).exclude(id_expediteur=user).count()

        conversations_data.append({
            'conversation': conv,
            'other_user': other_user,
            'last_message': last_message,
            'unread_count': unread_count,
        })

    # Trie par date du dernier message (plus récent en premier)
    conversations_data.sort(
        key=lambda x: x['last_message'].date_envoi if x['last_message'] else x['conversation'].date_creation,
        reverse=True
    )

    return render(request, 'messaging/liste_conversations.html', {
        'conversations_data': conversations_data,
    })


@login_required
def detail_conversation(request, id_conversation):
    """
    Affiche les messages d'une conversation et gère l'envoi de nouveaux messages.
    """
    conversation = get_object_or_404(Conversation, id_conversation=id_conversation)
    user = request.user

    # Vérifie que l'utilisateur fait bien partie de cette conversation
    if conversation.id_utilisateur1 != user and conversation.id_utilisateur2 != user:
        return redirect('messaging:liste_conversations')

    # Marque les messages reçus comme lus
    conversation.messages.filter(lu=False).exclude(id_expediteur=user).update(lu=True)

    messages_list = conversation.messages.all()  # déjà trié par date_envoi grâce au Meta.ordering
    other_user = conversation.get_other_participant(user)
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                id_conversation=conversation,
                id_expediteur=user,
                contenu=form.cleaned_data['contenu']
            )
            # Après envoi, on recharge la page (pattern POST-Redirect-GET)
            return redirect('messaging:detail_conversation', id_conversation=id_conversation)

    return render(request, 'messaging/detail_conversation.html', {
        'conversation': conversation,
        'messages_list': messages_list,
        'other_user': other_user,
        'form': form,
    })


@login_required
def demarrer_conversation(request, id_utilisateur):
    """
    Démarre ou rejoint une conversation avec un autre utilisateur,
    puis redirige directement vers cette conversation.
    Appelé depuis la page de profil ou de matching.
    """
    from django.contrib.auth import get_user_model
    User = get_user_model()

    other_user = get_object_or_404(User, pk=id_utilisateur)

    # On ne peut pas démarrer une conversation avec soi-même
    if other_user == request.user:
        return redirect('messaging:liste_conversations')

    conversation = get_or_create_conversation(request.user, other_user)
    return redirect('messaging:detail_conversation', id_conversation=conversation.id_conversation)


@login_required
def nouveaux_messages(request, id_conversation):
    """
    Vue AJAX : retourne les nouveaux messages d'une conversation depuis un certain ID.
    Utilisée pour le rafraîchissement en temps réel (polling).
    Paramètre GET : last_id = dernier id_message connu par le client.
    """
    conversation = get_object_or_404(Conversation, id_conversation=id_conversation)
    user = request.user

    if conversation.id_utilisateur1 != user and conversation.id_utilisateur2 != user:
        return JsonResponse({'error': 'Non autorisé'}, status=403)

    last_id = request.GET.get('last_id', 0)

    new_messages = conversation.messages.filter(
        id_message__gt=last_id
    ).values('id_message', 'contenu', 'date_envoi', 'lu', 'id_expediteur_id')

    # Marque les messages reçus comme lus
    conversation.messages.filter(
        id_message__gt=last_id, lu=False
    ).exclude(id_expediteur=user).update(lu=True)

    messages_data = []
    for msg in new_messages:
        messages_data.append({
            'id_message': msg['id_message'],
            'contenu': msg['contenu'],
            'date_envoi': msg['date_envoi'].strftime('%H:%M'),
            'is_mine': msg['id_expediteur_id'] == user.pk,
        })

    return JsonResponse({'messages': messages_data})