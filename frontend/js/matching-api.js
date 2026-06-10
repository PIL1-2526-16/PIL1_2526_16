const couleurs = [
  'var(--gradient)',
  'linear-gradient(135deg,#7c3aed,#a78bfa)',
  'linear-gradient(135deg,#0891b2,#06b6d4)',
  'linear-gradient(135deg,#059669,#34d399)',
  'linear-gradient(135deg,#dc2626,#f87171)',
];

function getInitiales(nom) {
  return nom.split(' ').map(n => n[0]).join('').toUpperCase();
}

function afficherResultats(data) {
  const list = document.getElementById('cardsList');
  list.innerHTML = '';

  data.resultats.forEach((r, i) => {
    const couleur = couleurs[i % couleurs.length];
    const initiales = getInitiales(r.mentor);
    const badges = r.competences.map(c =>
      `<span class="badge-mentor badge-blue">${c}</span>`
    ).join('');
    const creneauxBadges = r.creneaux.map(c =>
      `<span class="common-dispo"><i class="bi bi-clock me-1"></i>${c}</span>`
    ).join('');
    const skillsData = r.competences.map(c => c.toLowerCase()).join(' ');

    const card = `
      <div class="match-result-card" 
           data-type="mentor" 
           data-mode="online" 
           data-score="${r.score}" 
           data-skills="${skillsData}"
           onclick="window.location.href='chat.html'">
        <div class="d-flex gap-3">
          <div class="avatar-sm" style="background:${couleur};">${initiales}</div>
          <div style="flex:1; min-width:0;">
            <div class="d-flex justify-content-between align-items-start flex-wrap gap-1">
              <div>
                <div style="font-weight:700; font-size:1rem;">${r.mentor}</div>
                <div style="font-size:0.82rem; color:var(--gray-400);">${r.filiere} · L${r.niveau} · 
                  <span class="badge-mentor badge-blue" style="font-size:0.75rem;">Mentor</span>
                </div>
              </div>
              <div class="score-circle" style="flex-shrink:0;">${r.score}%</div>
            </div>
            <div style="font-size:0.75rem; color:var(--gray-400); margin:0.5rem 0 0.25rem; font-weight:600;">Compétences en commun</div>
            <div class="d-flex flex-wrap gap-1 mb-2">${badges}</div>
            <div style="font-size:0.75rem; color:var(--gray-400); margin-bottom:0.25rem; font-weight:600;">Disponibilités communes</div>
            <div class="d-flex flex-wrap gap-1 mb-2">${creneauxBadges}</div>
            <div class="score-bar"><div class="score-fill" style="width:${r.score}%;"></div></div>
            <div class="d-flex justify-content-end mt-2">
              <span style="font-size:0.82rem; color:var(--accent-dark); font-weight:600;">
                Contacter <i class="bi bi-arrow-right"></i>
              </span>
            </div>
          </div>
        </div>
      </div>`;
    list.innerHTML += card;
  });

  filterCards(); // appliquer les filtres après injection
}

fetch('http://127.0.0.1:8000/matching/mentors/')
  .then(res => res.json())
  .then(data => afficherResultats(data))
  .catch(err => console.error('Erreur API:', err));
  