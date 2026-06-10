/**
 * MentorLink — chat.js
 * Logique messagerie + modal planifier + gestion badges non lus
 */

const isMobile = () => window.innerWidth <= 768;

function openConversation(initials, name, bg) {
  // Mettre à jour l'en-tête de la conversation
  document.getElementById('chatAvatar').textContent = initials;
  document.getElementById('chatAvatar').style.background = bg;
  document.getElementById('chatName').textContent = name;
  document.getElementById('modalWith').textContent = 'Avec ' + name;

  // Marquer le contact actif + retirer son badge non lu
  document.querySelectorAll('.chat-contact').forEach(c => c.classList.remove('active'));
  const contact = event.currentTarget;
  contact.classList.add('active');

  const badge = contact.querySelector('.unread-badge');
  if (badge) {
    badge.remove();
    updateNavBadge();
  }

  // Sur mobile : masquer la sidebar et afficher la conversation
  if (isMobile()) {
    document.getElementById('sidebar').classList.add('hidden-mobile');
  }
}

function updateNavBadge() {
  // Recompter tous les badges restants dans la liste des contacts
  const remaining = document.querySelectorAll('.contacts-list .unread-badge').length;
  const navBadge  = document.querySelector('.nav-links .unread-badge');
  if (!navBadge) return;
  if (remaining === 0) {
    navBadge.remove();
  } else {
    navBadge.textContent = remaining;
  }
}

function showSidebar() {
  document.getElementById('sidebar').classList.remove('hidden-mobile');
}

function sendMessage() {
  const input = document.getElementById('msgInput');
  const text  = input.value.trim();
  if (!text) return;
  const area   = document.getElementById('messagesArea');
  const bubble = document.createElement('div');
  bubble.className   = 'chat-bubble-me';
  bubble.textContent = text;
  area.appendChild(bubble);
  input.value = '';
  area.scrollTop = area.scrollHeight;
}

function sendOnEnter(e) {
  if (e.key === 'Enter') sendMessage();
}

function openModal() {
  document.getElementById('planModal').style.display = 'flex';
  document.getElementById('confirmMsg').style.display = 'none';
}
function closeModal() {
  document.getElementById('planModal').style.display = 'none';
}
function closeModalOutside(e) {
  if (e.target === document.getElementById('planModal')) closeModal();
}
function confirmSession() {
  document.getElementById('confirmMsg').style.display = 'block';
  setTimeout(() => closeModal(), 1800);
}

document.addEventListener('DOMContentLoaded', () => {
  const area = document.getElementById('messagesArea');
  if (area) area.scrollTop = area.scrollHeight;
});
