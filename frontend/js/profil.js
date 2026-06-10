/**
 * MentorLink — profil.js
 * Logique page profil : édition des sections
 */

function toggleEdit(editId, viewId, btn) {
  const editEl = document.getElementById(editId);
  const viewEl = document.getElementById(viewId);
  const isEditing = editEl.style.display !== 'none';
  if (isEditing) {
    editEl.style.display = 'none';
    viewEl.style.display = '';
    btn.innerHTML = '<i class="bi bi-pencil me-1"></i>Modifier';
  } else {
    editEl.style.display = 'block';
    viewEl.style.display = 'none';
    btn.innerHTML = '<i class="bi bi-x me-1"></i>Annuler';
  }
}

function saveEdit(editId, viewId, btn) {
  document.getElementById(editId).style.display = 'none';
  document.getElementById(viewId).style.display = '';
  btn.innerHTML = '<i class="bi bi-pencil me-1"></i>Modifier';
}

function handlePhotoChange(event) {
  const file = event.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = function(e) {
    const avatarDisplay = document.getElementById('avatarDisplay');
    const avatarImg     = document.getElementById('avatarImg');
    avatarImg.src = e.target.result;
    avatarImg.style.display = 'block';
    avatarDisplay.style.display = 'none';
  };
  reader.readAsDataURL(file);
}
