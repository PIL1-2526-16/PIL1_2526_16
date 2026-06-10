/**
 * MentorLink — main.js
 * Scripts communs à toutes les pages
 */

// Déconnexion
function logout(url) {
  if (confirm('Tu veux vraiment te déconnecter ?')) {
    window.location.href = url;
  }
}

// Toggle affichage mot de passe
function togglePassword(inputId, iconId) {
  const input = document.getElementById(inputId);
  const icon  = document.getElementById(iconId);
  if (!input) return;
  if (input.type === 'password') {
    input.type = 'text';
    if (icon) icon.className = 'bi bi-eye-slash';
  } else {
    input.type = 'password';
    if (icon) icon.className = 'bi bi-eye';
  }
}

// Tags sélectionnables (register / profil)
function toggleTag(el) {
  el.classList.toggle('selected');
}

// Bascule entre la vue lecture et la vue édition d'une section de profil
function toggleEdit(editId, viewId, btn) {
  const editEl = document.getElementById(editId);
  const viewEl = document.getElementById(viewId);
  const showEdit = editEl.style.display === 'none';
  editEl.style.display = showEdit ? 'block' : 'none';
  viewEl.style.display = showEdit ? 'none' : 'block';
  if (btn) btn.style.display = showEdit ? 'none' : 'inline-flex';
}
