from django.db import models
from users.models import Utilisateur, Competence


class OffreMentorat(models.Model):
    TYPE_OFFRE = [
        ('offre', 'Offre (je propose mon aide)'),
        ('demande', 'Demande (je cherche un mentor)'),
    ]
    FORMATS = [
        ('présentiel', 'Présentiel'),
        ('en ligne', 'En ligne'),
        ('les deux', 'Les deux'),
    ]
    STATUTS = [
        ('ouverte', 'Ouverte'),
        ('fermée', 'Fermée'),
    ]

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='offres')
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, related_name='offres')
    type_offre = models.CharField(max_length=10, choices=TYPE_OFFRE)
    format = models.CharField(max_length=12, choices=FORMATS)
    statut = models.CharField(max_length=10, choices=STATUTS, default='ouverte')
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur} - {self.competence} ({self.type_offre})"


class Matching(models.Model):
    STATUTS = [
        ('proposé', 'Proposé'),
        ('accepté', 'Accepté'),
        ('refusé', 'Refusé'),
    ]

    mentor = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='matchings_mentor')
    mentore = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='matchings_mentore')
    offre = models.ForeignKey(OffreMentorat, on_delete=models.CASCADE, related_name='matchings', null=True, blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    statut = models.CharField(max_length=10, choices=STATUTS, default='proposé')
    date_matching = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(condition=~models.Q(mentor=models.F('mentore')), name='mentor_diff_mentore'),
        ]

    def __str__(self):
        return f"{self.mentor} <-> {self.mentore} ({self.score}%)"
