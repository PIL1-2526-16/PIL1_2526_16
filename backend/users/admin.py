from django.contrib import admin
from .models import Utilisateur, Disponibilite, Competence, Categorie, UtilisateurCompetence

admin.site.register(Utilisateur)
admin.site.register(Disponibilite)
admin.site.register(Competence)
admin.site.register(Categorie)
admin.site.register(UtilisateurCompetence)