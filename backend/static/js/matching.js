/**
 * MentorLink — matching.js
 * Filtres, recherche, modals offre/demande
 */

let activeType  = 'all';
let activeSkill = '';

function setFilter(el, type) {
  document.querySelectorAll('.filter-bar .filter-chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
  activeType  = type;
  activeSkill = '';
  document.querySelectorAll('.card-mentor .filter-chip').forEach(c => c.classList.remove('active'));
  filterCards();
}

function filterBySkill(el, skill) {
  document.querySelectorAll('.card-mentor .filter-chip').forEach(c => c.classList.remove('active'));
  activeSkill = activeSkill === skill ? '' : skill;
  if (activeSkill) el.classList.add('active');
  filterCards();
}

function filterCards() {
  const search = (document.getElementById('searchInput') || { value: '' }).value.toLowerCase();
  const cards  = document.querySelectorAll('.match-result-card');
  let visible  = 0;
  cards.forEach(card => {
    const type   = card.dataset.type;
    const mode   = card.dataset.mode;
    const skills = card.dataset.skills;
    const text   = card.innerText.toLowerCase();
    const typeOk   = activeType === 'all' || type === activeType
                     || (activeType === 'online' && mode === 'online')
                     || (activeType === 'presentiel' && mode === 'presentiel');
    const skillOk  = !activeSkill || skills.includes(activeSkill);
    const searchOk = !search || text.includes(search);
    if (typeOk && skillOk && searchOk) { card.classList.remove('hidden'); visible++; }
    else                               { card.classList.add('hidden'); }
  });
  const rc = document.getElementById('resultCount');
  if (rc) rc.innerHTML = '<strong style="color:var(--gray-800);">' + visible + ' résultat' + (visible > 1 ? 's' : '') + '</strong> correspondant à ton profil';
  const es = document.getElementById('emptyState');
  if (es) es.style.display = visible === 0 ? 'block' : 'none';
}

function sortByScore() {
  const list  = document.getElementById('cardsList');
  const cards = Array.from(list.querySelectorAll('.match-result-card'));
  cards.sort((a, b) => parseInt(b.dataset.score) - parseInt(a.dataset.score));
  cards.forEach(c => list.appendChild(c));
}

// Modals Offre / Demande
function openOfferModal(type) {
  document.getElementById('offerModalTitle').textContent = type === 'offre' ? 'Publier une offre de mentorat' : 'Publier une demande de mentorat';
  document.getElementById('offerModalSubtitle').textContent = type === 'offre'
    ? 'Propose tes compétences à des étudiants qui en ont besoin.'
    : 'Indique ce que tu cherches à apprendre et trouve un mentor.';
  document.getElementById('offerModal').style.display = 'flex';
  document.getElementById('offerConfirm').style.display = 'none';
}
function closeOfferModal() {
  document.getElementById('offerModal').style.display = 'none';
}
function closeOfferOutside(e) {
  if (e.target === document.getElementById('offerModal')) closeOfferModal();
}
function submitOffer() {
  document.getElementById('offerConfirm').style.display = 'block';
  setTimeout(() => closeOfferModal(), 1800);
}
