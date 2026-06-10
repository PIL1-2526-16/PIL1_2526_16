# FORMULAIRES
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from .models import Utilisateur, Disponibilite, UtilisateurCompetence, Competence


# INSCRIPTION
class InscriptionForm(UserCreationForm):
    telephone = forms.CharField(max_length=20)
    photo_profil = forms.ImageField(required=False)
    filiere = forms.ChoiceField(choices=[
        ('IA', 'IA'), ('IM', 'IM'), ('GL', 'GL'),
        ('SE&IoT', 'SE&IoT'), ('SI', 'SI')
    ])
    niveau = forms.ChoiceField(choices=[
        ('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3')
    ])
    bio = forms.CharField(widget=forms.Textarea, required=False)
    centres_interet = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'email', 'telephone', 'password1', 
                  'password2', 'photo_profil', 'filiere', 'niveau', 
                  'bio', 'centres_interet']
        

# CONNEXION
class ConnexionForm(AuthenticationForm):
    username = forms.CharField(
        label="Email ou téléphone",
        widget=forms.TextInput(attrs={'placeholder': 'Email ou numéro de téléphone'})
    )

# MODIFICATION DU PROFIL
class ModificationProfilForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'telephone', 'photo_profil', 'filiere', 'niveau', 'bio', 'centres_interet']


# CHANGEMENT DE MOT DE PASSE (utilisateur connecté)
class ChangerMotDePasseForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Mot de passe actuel",
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe actuel'})
    )
    new_password1 = forms.CharField(
        label="Nouveau mot de passe",
        widget=forms.PasswordInput(attrs={'placeholder': 'Nouveau mot de passe'})
    )
    new_password2 = forms.CharField(
        label="Confirmer le nouveau mot de passe",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le nouveau mot de passe'})
    )


# REINITIALISATION DU PROFIL
class DemandeReinitialisationForm(PasswordResetForm):
    email = forms.EmailField(
        label="Adresse email",
        widget=forms.EmailInput(attrs={'placeholder': 'Votre adresse email'})
    )

class NouveauMotDePasseForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Nouveau mot de passe",
        widget=forms.PasswordInput(attrs={'placeholder': 'Nouveau mot de passe'})
    )
    new_password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe'})
    )
