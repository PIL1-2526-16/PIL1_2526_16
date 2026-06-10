from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, mot_de_passe=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(mot_de_passe)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mot_de_passe=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, mot_de_passe, **extra_fields)


# CHAMPS DE LA TABLE UTILISATEUR
class Utilisateur(AbstractBaseUser, PermissionsMixin):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    telephone = models.CharField(max_length=20, unique=True)
    photo_profil = models.ImageField(upload_to='photos/', blank=True, null=True)
    filiere = models.CharField(max_length=10, choices=[
        ('IA', 'IA'), ('IM', 'IM'), ('GL', 'GL'),
        ('SEIoT', 'SEIoT'), ('SI', 'SI')
    ])
    niveau = models.CharField(max_length=2, choices=[
        ('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3')
    ])
    bio = models.TextField(blank=True, null=True)
    centres_interet = models.TextField(blank=True, null=True)
    date_inscription = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # IDENTIFIANT PRINCIPAL 
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nom', 'prenom', 'telephone']

    objects = UtilisateurManager()


    # COMMENT UN UTILISATEUR S'AFFICHE (ICI : Prénom Nom)
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    

# CHAMPS DES TABLES DISPONIBILITE ET COMPETENCES
# DISPONIBILITE
class Disponibilite(models.Model):
    JOURS = [
        ('Lundi', 'Lundi'), ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche')
    ]
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='disponibilites')
    jour = models.CharField(max_length=10, choices=JOURS)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    # COMMENT LA DISPONIBILITE S'AFFICHE (ICI : Prénom Nom)
    def __str__(self):
        return f"{self.utilisateur} - {self.jour} {self.heure_debut}-{self.heure_fin}"

# COMPETENCES
class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom_categorie

class Competence(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='competences')
    nom_competence = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nom_competence


class UtilisateurCompetence(models.Model):
    TYPES = [
        ('point_fort', 'Point fort'),
        ('point_faible', 'Point faible')
    ]
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='competences')
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, related_name='utilisateurs')
    type_competence = models.CharField(max_length=20, choices=TYPES)

    class Meta:
        unique_together = ('utilisateur', 'competence', 'type_competence')

    def __str__(self):
        return f"{self.utilisateur} - {self.competence} ({self.type_competence})"