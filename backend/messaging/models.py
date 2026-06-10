from django.db import models
from users.models import Utilisateur


class Conversation(models.Model):
    utilisateur1 = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='conversations1')
    utilisateur2 = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='conversations2')
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(condition=~models.Q(utilisateur1=models.F('utilisateur2')), name='participants_differents'),
        ]
        unique_together = ('utilisateur1', 'utilisateur2')

    def autre_participant(self, utilisateur):
        return self.utilisateur2 if self.utilisateur1_id == utilisateur.id else self.utilisateur1

    def __str__(self):
        return f"{self.utilisateur1} <-> {self.utilisateur2}"


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_envoyes')
    contenu = models.TextField(blank=True)
    fichier = models.FileField(upload_to='messages/', blank=True, null=True)
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_envoi']

    def nom_fichier(self):
        return self.fichier.name.split('/')[-1] if self.fichier else ''

    def est_image(self):
        return self.fichier and self.fichier.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))

    def __str__(self):
        return f"{self.expediteur} : {self.contenu[:30]}"
