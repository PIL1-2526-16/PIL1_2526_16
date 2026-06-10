from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (InscriptionForm, ConnexionForm, ModificationProfilForm,
                    DemandeReinitialisationForm, NouveauMotDePasseForm)
from .models import Utilisateur, Disponibilite, UtilisateurCompetence
from .models import Utilisateur, Disponibilite, UtilisateurCompetence, Competence


# ACCUEIL
def accueil(request):
    return render(request, 'users/accueil.html')


# INSCRIPTION
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            utilisateur = form.save()
            login(request, utilisateur)
            messages.success(request, "Inscription réussie. Bienvenue !")
            return redirect('profil')
    else:
        form = InscriptionForm()
    return render(request, 'users/inscription.html', {'form': form})


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
        'competences': competences
    })


# MODIFICATION PROFIL
@login_required
def modifier_profil(request):
    competences_disponibles = Competence.objects.all()
    competences_actuelles = UtilisateurCompetence.objects.filter(
        utilisateur=request.user
    ).values_list('competence', flat=True)

    if request.method == 'POST':
        form = ModificationProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            
            # Mise à jour des disponibilités
            Disponibilite.objects.filter(utilisateur=request.user).delete()
            jours = request.POST.getlist('jours')
            heures_debut = request.POST.getlist('heures_debut')
            heures_fin = request.POST.getlist('heures_fin')
            for i in range(len(jours)):
                if heures_debut[i] and heures_fin[i]:
                    Disponibilite.objects.create(
                        utilisateur=request.user,
                        jour=jours[i],
                        heure_debut=heures_debut[i],
                        heure_fin=heures_fin[i]
                    )
            
            # Mise à jour des compétences
            UtilisateurCompetence.objects.filter(utilisateur=request.user).delete()
            competences_selectionnees = request.POST.getlist('competences')
            type_competence = request.POST.get('type_competence')
            for id_competence in competences_selectionnees:
                UtilisateurCompetence.objects.create(
                    utilisateur=request.user,
                    competence_id=id_competence,
                    type_competence=type_competence
                )
            
            messages.success(request, "Profil mis à jour avec succès.")
            return redirect('profil')
    else:
        form = ModificationProfilForm(instance=request.user)
    
    return render(request, 'users/modifier_profil.html', {
        'form': form,
        'competences_disponibles': competences_disponibles,
        'competences_actuelles': competences_actuelles
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
