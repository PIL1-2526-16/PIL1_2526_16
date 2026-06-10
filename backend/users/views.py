from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (InscriptionForm, ConnexionForm, ModificationProfilForm,
                    ChangerMotDePasseForm, DemandeReinitialisationForm, NouveauMotDePasseForm)
from .models import Utilisateur, Disponibilite, UtilisateurCompetence


# ACCUEIL
def accueil(request):
    mentors = Utilisateur.objects.order_by('-date_inscription')[:3]
    return render(request, 'users/accueil.html', {'mentors': mentors})


# TABLEAU DE BORD
@login_required
def tableau_de_bord(request):
    from matching.models import Matching, OffreMentorat
    from messaging.models import Message
    utilisateur = request.user

    matchings_acceptes = Matching.objects.filter(
        (models.Q(mentor=utilisateur) | models.Q(mentore=utilisateur)),
        statut='accepté'
    ).order_by('-score')

    matchings = [
        {'autre': m.mentore if m.mentor_id == utilisateur.id else m.mentor, 'score': m.score}
        for m in matchings_acceptes[:5]
    ]

    nb_demandes_recues = Matching.objects.filter(mentor=utilisateur, statut='proposé').count()

    messages_non_lus = Message.objects.filter(
        conversation__utilisateur1=utilisateur
    ).exclude(expediteur=utilisateur).filter(lu=False).count()
    messages_non_lus += Message.objects.filter(
        conversation__utilisateur2=utilisateur
    ).exclude(expediteur=utilisateur).filter(lu=False).count()

    return render(request, 'users/tableau_de_bord.html', {
        'utilisateur': utilisateur,
        'matchings': matchings,
        'nb_matchings': matchings_acceptes.count(),
        'nb_offres': OffreMentorat.objects.filter(utilisateur=utilisateur).count(),
        'nb_competences': UtilisateurCompetence.objects.filter(utilisateur=utilisateur).count(),
        'messages_non_lus': messages_non_lus,
        'nb_demandes_recues': nb_demandes_recues,
    })


# ENREGISTREMENT COMPETENCES / DISPONIBILITES (partagé inscription + page dédiée)
def _enregistrer_competences_disponibilites(post_data, utilisateur):
    Disponibilite.objects.filter(utilisateur=utilisateur).delete()
    jours = post_data.getlist('jours')
    heures_debut = post_data.getlist('heures_debut')
    heures_fin = post_data.getlist('heures_fin')
    for i in range(len(jours)):
        if heures_debut[i] and heures_fin[i]:
            Disponibilite.objects.create(
                utilisateur=utilisateur,
                jour=jours[i],
                heure_debut=heures_debut[i],
                heure_fin=heures_fin[i]
            )

    UtilisateurCompetence.objects.filter(utilisateur=utilisateur).delete()
    points_forts_ids = set(post_data.getlist('points_forts'))
    points_faibles_ids = set(post_data.getlist('points_faibles')) - points_forts_ids
    for competence_id in points_forts_ids:
        UtilisateurCompetence.objects.create(
            utilisateur=utilisateur, competence_id=competence_id, type_competence='point_fort'
        )
    for competence_id in points_faibles_ids:
        UtilisateurCompetence.objects.create(
            utilisateur=utilisateur, competence_id=competence_id, type_competence='point_faible'
        )


# INSCRIPTION
def inscription(request):
    from .models import Categorie

    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            utilisateur = form.save()
            login(request, utilisateur)
            _enregistrer_competences_disponibilites(request.POST, utilisateur)
            messages.success(request, "Inscription réussie. Bienvenue !")
            return redirect('profil')
    else:
        form = InscriptionForm()

    return render(request, 'users/inscription.html', {
        'form': form,
        'categories': Categorie.objects.prefetch_related('competences'),
        'jours_choices': Disponibilite.JOURS,
    })


# CONNEXION
def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request, data=request.POST)
        if form.is_valid():
            utilisateur = form.get_user()
            login(request, utilisateur)
            messages.success(request, "Connexion réussie.")
            return redirect('profil')
        else:
            messages.error(request, "Identifiant ou mot de passe incorrect.")
    else:
        form = ConnexionForm()
    return render(request, 'users/connexion.html', {'form': form})


# DECONNEXION
def deconnexion(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté.")
    return redirect('connexion')


# PROFIL
@login_required
def profil(request):
    utilisateur = request.user
    disponibilites = Disponibilite.objects.filter(utilisateur=utilisateur)
    competences = UtilisateurCompetence.objects.filter(utilisateur=utilisateur)
    return render(request, 'users/profil.html', {
        'utilisateur': utilisateur,
        'disponibilites': disponibilites,
        'competences': competences,
        'edit_form': ModificationProfilForm(instance=utilisateur),
    })


# MODIFICATION PROFIL
@login_required
def modifier_profil(request):
    if request.method == 'POST':
        form = ModificationProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil mis à jour avec succès.")
            return redirect('profil')
    else:
        form = ModificationProfilForm(instance=request.user)

    return render(request, 'users/modifier_profil.html', {'form': form})


# CHANGEMENT DE MOT DE PASSE
@login_required
def changer_mot_de_passe(request):
    if request.method == 'POST':
        form = ChangerMotDePasseForm(request.user, request.POST)
        if form.is_valid():
            utilisateur = form.save()
            update_session_auth_hash(request, utilisateur)
            messages.success(request, "Mot de passe modifié avec succès.")
            return redirect('profil')
    else:
        form = ChangerMotDePasseForm(request.user)

    return render(request, 'users/changer_mot_de_passe.html', {'form': form})


# GESTION DES COMPETENCES ET DISPONIBILITES
@login_required
def gerer_competences(request):
    from .models import Categorie

    if request.method == 'POST':
        _enregistrer_competences_disponibilites(request.POST, request.user)
        messages.success(request, "Compétences et disponibilités mises à jour avec succès.")
        return redirect('profil')

    mes_competences = UtilisateurCompetence.objects.filter(utilisateur=request.user)

    return render(request, 'users/gerer_competences.html', {
        'categories': Categorie.objects.prefetch_related('competences'),
        'points_forts_ids': set(mes_competences.filter(type_competence='point_fort').values_list('competence_id', flat=True)),
        'points_faibles_ids': set(mes_competences.filter(type_competence='point_faible').values_list('competence_id', flat=True)),
        'disponibilites': Disponibilite.objects.filter(utilisateur=request.user),
        'jours_choices': Disponibilite.JOURS,
    })


# REINITIALISATION DE MOT DE PASSE
def demande_reinitialisation(request):
    if request.method == 'POST':
        form = DemandeReinitialisationForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                email_template_name='users/email_reinitialisation.html'
            )
            messages.success(request, "Un lien de réinitialisation a été envoyé à votre adresse email.")
            return redirect('connexion')
    else:
        form = DemandeReinitialisationForm()
    return render(request, 'users/demande_reinitialisation.html', {'form': form})


def nouveau_mot_de_passe(request, uidb64, token):
    if request.method == 'POST':
        form = NouveauMotDePasseForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mot de passe modifié avec succès.")
            return redirect('connexion')
    else:
        form = NouveauMotDePasseForm(request.user)
    return render(request, 'users/nouveau_mot_de_passe.html', {'form': form}) 
