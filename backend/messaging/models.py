from django.db import models
from django.conf import settings


class Conversation(models.Model):
    id_conversation = models.AutoField(primary_key=True)
    id_utilisateur1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='conversations_comme_utilisateur1',
        db_column='id_utilisateur1'
    )
    id_utilisateur2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='conversations_comme_utilisateur2',
        db_column='id_utilisateur2'
    )
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'CONVERSATION'
        managed = False  

    def get_other_participant(self, user):
        """Retourne l'autre participant de la conversation."""
        if self.id_utilisateur1 == user:
            return self.id_utilisateur2
        return self.id_utilisateur1

    def __str__(self):
        return f"Conversation {self.id_conversation}"


class Message(models.Model):
    id_message = models.AutoField(primary_key=True)
    id_conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages',
        db_column='id_conversation'
    )
    id_expediteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='messages_envoyes',
        db_column='id_expediteur'
    )
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    class Meta:
        db_table = 'MESSAGE'
        managed = False
        ordering = ['date_envoi']  # Les messages s'affichent du plus ancien au plus récent

    def __str__(self):
        return f"Message {self.id_message} de {self.id_expediteur}"