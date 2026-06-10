/**
 * MentorLink — register.js
 * Logique inscription : étapes + exclusion mutuelle points forts/faibles
 */

const CATEGORIES = [
  { title: 'Programmation',         skills: ['Python','Java','C / C++','JavaScript','PHP','Rust'] },
  { title: 'Web & Mobile',          skills: ['HTML / CSS','React','Django','Flutter','Node.js'] },
  { title: 'Bases de données',      skills: ['SQL','MySQL','PostgreSQL','MongoDB','Merise / UML'] },
  { title: 'Algorithmique & Maths', skills: ['Algorithmique','Structures de données','Mathématiques discrètes','Algèbre linéaire','Probabilités & Statistiques'] },
  { title: 'Réseaux & Systèmes',    skills: ['Réseaux','Linux','Administration système','Protocoles TCP/IP'] },
  { title: 'Intelligence Artificielle', skills: ['Machine Learning','Deep Learning','NLP','Computer Vision'] },
  { title: 'Sécurité',              skills: ['Cybersécurité','Cryptographie','Ethical Hacking'] },
  { title: 'Génie Logiciel',        skills: ['Git / GitHub','Génie logiciel','Tests & Qualité','DevOps'] },
];

function buildTags() {
  const sDiv = document.getElementById('strengths');
  const wDiv = document.getElementById('weaknesses');
  if (!sDiv || !wDiv) return;

  CATEGORIES.forEach(cat => {
    [sDiv, wDiv].forEach(container => {
      const label = document.createElement('div');
      label.className = 'category-title';
      label.textContent = cat.title;
      container.appendChild(label);
    });

    cat.skills.forEach(skill => {
      const key = skill.toLowerCase();

      const ts = document.createElement('span');
      ts.className = 'tag-skill';
      ts.textContent = skill;
      ts.dataset.key = key;

      const tw = document.createElement('span');
      tw.className = 'tag-skill';
      tw.textContent = skill;
      tw.dataset.key = key;

      ts.onclick = () => {
        ts.classList.toggle('selected');
        if (ts.classList.contains('selected')) {
          tw.classList.add('disabled');
          tw.classList.remove('selected');
        } else {
          tw.classList.remove('disabled');
        }
      };

      tw.onclick = () => {
        tw.classList.toggle('selected');
        if (tw.classList.contains('selected')) {
          ts.classList.add('disabled');
          ts.classList.remove('selected');
        } else {
          ts.classList.remove('disabled');
        }
      };

      sDiv.appendChild(ts);
      wDiv.appendChild(tw);
    });
  });
}

function goToStep(n) {
  [1, 2, 3].forEach(i => {
    document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
  });
  for (let i = 1; i <= 3; i++) {
    const s = document.getElementById('s' + i);
    if (i < n)      { s.className = 'step done'; s.innerHTML = '<i class="bi bi-check" style="font-size:0.75rem;"></i>'; }
    else if (i === n) { s.className = 'step active'; s.textContent = i; }
    else            { s.className = 'step pending'; s.textContent = i; }
  }
  for (let i = 1; i <= 2; i++) {
    document.getElementById('l' + i).className = i < n ? 'step-line done' : 'step-line';
  }
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

document.addEventListener('DOMContentLoaded', buildTags);
