from django.db import models as db_models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from users.models import Utilisateur, Disponibilite, UtilisateurCompetence
from .models import OffreMentorat, Matching
from .forms import OffreMentoratForm


def calculer_score(utilisateur, autre):
    """Calcule un score de compatibilité (0-100) entre deux utilisateurs."""
    forts_u = set(UtilisateurCompetence.objects.filter(
        utilisateur=utilisateur, type_competence='point_fort'
    ).values_list('competence_id', flat=True))
    faibles_u = set(UtilisateurCompetence.objects.filter(
        utilisateur=utilisateur, type_competence='point_faible'
    ).values_list('competence_id', flat=True))
    forts_a = set(UtilisateurCompetence.objects.filter(
        utilisateur=autre, type_competence='point_fort'
    ).values_list('competence_id', flat=True))
    faibles_a = set(UtilisateurCompetence.objects.filter(
        utilisateur=autre, type_competence='point_faible'
    ).values_list('competence_id', flat=True))

    competences_communes_ids = (forts_u & faibles_a) | (forts_a & faibles_u)
    score = min(len(competences_communes_ids), 5) * 10  # jusqu'à 50 points

    dispos_u = Disponibilite.objects.filter(utilisateur=utilisateur)
    jours_u = set(dispos_u.values_list('jour', flat=True))
    jours_a = set(Disponibilite.objects.filter(utilisateur=autre).values_list('jour', flat=True))
    jours_communs = jours_u & jours_a
    score += min(len(jours_communs), 3) * 10  # jusqu'à 30 points

    if utilisateur.filiere == autre.filiere:
        score += 10
    if utilisateur.niveau == autre.niveau:
        score += 10

    from users.models import Competence
    competences_communes = Competence.objects.filter(id__in=competences_communes_ids)

    dispos_communes = []
    for jour in sorted(jours_communs):
        dispo = dispos_u.filter(jour=jour).first()
        if dispo and dispo.heure_debut.minute:
            heure = dispo.heure_debut.strftime('%Hh%M')
        elif dispo:
            heure = dispo.heure_debut.strftime('%Hh')
        else:
            heure = ''
        dispos_communes.append(f"{jour[:3]} {heure}".strip())

    return min(score, 100), competences_communes, dispos_communes


@login_required
def liste(request):
    utilisateur = request.user
    autres = Utilisateur.objects.exclude(id=utilisateur.id)

    matchings_existants = Matching.objects.filter(
        db_models.Q(mentor=utilisateur) | db_models.Q(mentore=utilisateur)
    )
    matching_par_utilisateur = {}
    for m in matchings_existants:
        autre_id = m.mentore_id if m.mentor_id == utilisateur.id else m.mentor_id
        matching_par_utilisateur[autre_id] = m

    resultats = []
    for autre in autres:
        score, competences_communes, dispos_communes = calculer_score(utilisateur, autre)
        if score > 0:
            formats_autre = set(OffreMentorat.objects.filter(utilisateur=autre, statut='ouverte').values_list('format', flat=True))
            resultats.append({
                'utilisateur': autre,
                'score': score,
                'competences_communes': competences_communes,
                'jours_communs': dispos_communes,
                'en_ligne': 'en ligne' in formats_autre or 'les deux' in formats_autre,
                'presentiel': 'présentiel' in formats_autre or 'les deux' in formats_autre,
                'matching': matching_par_utilisateur.get(autre.id),
            })

    resultats.sort(key=lambda r: r['score'], reverse=True)

    if request.method == 'POST':
        offre_form = OffreMentoratForm(request.POST)
        if offre_form.is_valid():
            offre = offre_form.save(commit=False)
            offre.utilisateur = utilisateur
            offre.save()
            messages.success(request, "Votre offre de mentorat a été publiée.")
            return redirect('matching:liste')
    else:
        offre_form = OffreMentoratForm()

    mes_offres = OffreMentorat.objects.filter(utilisateur=utilisateur).order_by('-date_publication')

    demandes_recues = Matching.objects.filter(mentor=utilisateur, statut='proposé')
    matchings_acceptes = matchings_existants.filter(statut='accepté')

    return render(request, 'matching/liste.html', {
        'resultats': resultats,
        'offre_form': offre_form,
        'mes_offres': mes_offres,
        'demandes_recues': demandes_recues,
        'matchings_acceptes': matchings_acceptes,
    })


@login_required
def proposer(request, utilisateur_id):
    autre = get_object_or_404(Utilisateur, id=utilisateur_id)

    if autre == request.user:
        messages.error(request, "Vous ne pouvez pas vous proposer un matching à vous-même.")
        return redirect('matching:liste')

    score, _, _ = calculer_score(request.user, autre)

    if not Matching.objects.filter(mentor=autre, mentore=request.user).exists() and \
       not Matching.objects.filter(mentor=request.user, mentore=autre).exists():
        Matching.objects.create(
            mentor=autre,
            mentore=request.user,
            score=score,
            statut='proposé',
        )
        messages.success(request, f"Une demande de mentorat a été envoyée à {autre}.")
    else:
        messages.info(request, "Un matching existe déjà avec cette personne.")

    return redirect('matching:liste')


@login_required
@require_POST
def accepter(request, matching_id):
    matching = get_object_or_404(Matching, id=matching_id, mentor=request.user, statut='proposé')
    matching.statut = 'accepté'
    matching.save()
    messages.success(request, f"Tu as accepté la demande de matching de {matching.mentore}.")
    return redirect('matching:liste')


@login_required
@require_POST
def refuser(request, matching_id):
    matching = get_object_or_404(Matching, id=matching_id, mentor=request.user, statut='proposé')
    matching.statut = 'refusé'
    matching.save()
    messages.info(request, f"Tu as refusé la demande de matching de {matching.mentore}.")
    return redirect('matching:liste')
