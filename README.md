# MentorLink — Projet Intégrateur L1 2025-2026

> Plateforme web de mentorat académique et professionnel pour les étudiants de l'IFRI

**Université d'Abomey-Calavi — Institut de Formation et de Recherche en Informatique (IFRI)**
Projet Intégrateur · Licence 1 · Année académique 2025-2026
Groupe : **PIL1_2526_16**

---

## Table des matières

1. [Présentation du projet](#1-présentation-du-projet)
2. [Équipe et organisation](#2-équipe-et-organisation)
3. [Fonctionnalités](#3-fonctionnalités)
4. [Architecture et conception](#4-architecture-et-conception)
5. [Structure du dépôt](#5-structure-du-dépôt)
6. [Base de données](#6-base-de-données)
7. [Instructions de déploiement](#7-instructions-de-déploiement)
8. [Manuel d'utilisation](#8-manuel-dutilisation)
9. [Technologies utilisées](#9-technologies-utilisées)

---

## 1. Présentation du projet

**MentorLink** est une application web qui met en relation les étudiants de l'IFRI souhaitant bénéficier ou offrir du mentorat académique et professionnel.

Chaque utilisateur crée un profil indiquant ses compétences, ses lacunes et ses disponibilités. Un algorithme de matching propose automatiquement les combinaisons mentor-mentoré les plus pertinentes selon la compatibilité des compétences, la proximité des filières et la compatibilité horaire. Une messagerie intégrée permet d'organiser et de suivre les sessions de mentorat.

### Modules développés

| Module | Description |
|---|---|
| **Gestion des comptes et profils** | Inscription, connexion, profil utilisateur complet |
| **Mise en correspondance** | Algorithme de matching, offres et demandes de mentorat |
| **Messagerie instantanée** | Chat en temps réel, historique des conversations, notifications |

---

## 2. Équipe et organisation

### Membres du groupe

| Membre | Filière | Rôle principal |
|---|---|---|
| **Charbelle MEVO** | Sécurité Informatique | Frontend (HTML/CSS/JS) & GitHub |
| **Ingrid GONÇALVES** | Systèmes Embarqués & IoT | Backend principal (Python/Django) |
| **Richard TCHEKPO** | Sécurité Informatique | Base de données (fichier .sql) |
| **N'KOUEI Priscille** | Internet et Multimédia | Frontend & Rapport HTML |
| **AHOUANSOU Owen** | Génie Logiciel | Support backend |
| **ALLADE Majolain** | Génie Logiciel | Support backend (avec Ingrid) |
| **SOSSOU Théodote** | Intelligence Artificielle | Support base de données (avec Richard) |

### Mode de fonctionnement interne

Le groupe a adopté une organisation basée sur la séparation claire des responsabilités :

- **Charbelle MEVO** gère le dépôt GitHub (création, protection de la branche `main`, accès collaborateurs) et développe toutes les interfaces utilisateur en HTML, CSS modulaire et JavaScript.
- **Ingrid GONÇALVES**, **AHOUANSOU Owen** et **ALLADE Majolain** travaillent ensemble sur le backend Python/Django : routes API, modèles de données, authentification, algorithme de matching et messagerie.
- **Richard TCHEKPO** et **SOSSOU Théodote** conçoivent la base de données relationnelle : MCD, MLD, puis le fichier `.sql` final avec toutes les tables et contraintes.
- **N'KOUEI Priscille** collabore avec Charbelle sur le frontend et prend en charge la rédaction du rapport HTML du projet.

Chaque membre travaille sur sa propre branche Git et soumet des Pull Requests vers `main`. Les fusions sont validées par Charbelle en tant que responsable GitHub du groupe.

---

## 3. Fonctionnalités

### Gestion des comptes et profils

- Inscription avec nom, prénom, email, téléphone, mot de passe
- Vérification de l'unicité de l'email et du téléphone
- Sélection des points forts et points faibles dès l'inscription
- Connexion via email ou téléphone
- Réinitialisation du mot de passe
- Profil modifiable : filière, niveau, compétences, disponibilités, bio, photo

### Mise en correspondance

- Publication d'offres et de demandes de mentorat (matières, horaires, format)
- Recherche filtrée par matière et disponibilité
- Algorithme de matching calculant un score de compatibilité selon :
  - Les compétences et matières communes
  - La compatibilité des horaires
  - La proximité de filière et de niveau
- Affichage des résultats avec score, compétences communes et disponibilités

### Messagerie

- Envoi et réception de messages texte
- Notifications en temps réel à la réception
- Historique des conversations conservé
- Liste des conversations accessible

### Sécurité

- Mots de passe hashés
- Authentification sécurisée par session
- Accès aux données personnelles restreint

---

## 4. Architecture et conception

### Architecture logicielle

L'application suit une architecture **client-serveur** :

```
Navigateur (Client)          Serveur Python/Django        Base de données
      │                              │                          │
      │  Requête HTTP/HTTPS          │                          │
      │ ─────────────────────────>   │                          │
      │                              │   Requête SQL            │
      │                              │ ───────────────────────> │
      │                              │   Résultat               │
      │                              │ <─────────────────────── │
      │  Réponse JSON / HTML         │                          │
      │ <─────────────────────────   │                          │
```

### Architecture CSS modulaire

Le CSS est découpé en fichiers séparés — **un fichier = une responsabilité** :

| Fichier | Responsabilité | Pages concernées |
|---|---|---|
| `base.css` | Variables CSS, reset, typographie globale | Toutes |
| `buttons.css` | Boutons, chips, tags de compétences | Toutes |
| `navbar.css` | Barre de navigation sticky, logo, menu mobile | Toutes |
| `forms.css` | Inputs, selects, textarea, labels, erreurs | login, register, profil |
| `cards.css` | Cartes mentor, résultats matching, statistiques | index, matching, profil |
| `auth.css` | Layout pages login et register | login, register |
| `hero.css` | Hero, sections et footer de la page d'accueil | index |
| `profil.css` | En-tête profil, disponibilités, bio, stats | profil |
| `matching.css` | Barre de filtres, layout 2 colonnes, résultats | matching |
| `chat.css` | Contacts sidebar, bulles messages, zone de saisie | chat |

### Ordre d'import CSS dans chaque page

```html
<!-- Fichiers communs — toujours dans cet ordre -->
<link rel="stylesheet" href="../css/base.css" />
<link rel="stylesheet" href="../css/buttons.css" />
<link rel="stylesheet" href="../css/navbar.css" />
<link rel="stylesheet" href="../css/forms.css" />
<link rel="stylesheet" href="../css/cards.css" />

<!-- Fichier spécifique à la page -->
<link rel="stylesheet" href="../css/hero.css" />      <!-- index.html -->
<link rel="stylesheet" href="../css/auth.css" />      <!-- login.html, register.html -->
<link rel="stylesheet" href="../css/profil.css" />    <!-- profil.html -->
<link rel="stylesheet" href="../css/matching.css" />  <!-- matching.html -->
<link rel="stylesheet" href="../css/chat.css" />      <!-- chat.html -->
```

### Palette de couleurs

| Variable | Valeur | Usage |
|---|---|---|
| `--color-primary` | `#1a6fc4` | Couleur principale, boutons, liens |
| `--color-secondary` | `#0ea5e9` | Fin du dégradé |
| `--color-primary-light` | `#e8f1fb` | Fonds légers, badges |
| `--color-gray-800` | `#1e293b` | Texte principal |
| `--color-gray-400` | `#94a3b8` | Texte secondaire |
| `--color-success` | `#22c55e` | Indicateur en ligne |
| `--color-danger` | `#ef4444` | Erreurs formulaire |

**Dégradé principal :** `linear-gradient(135deg, #1a6fc4 0%, #0ea5e9 100%)`
**Police :** Poppins (Google Fonts) — poids 300, 400, 500, 600, 700

---

## 5. Structure du dépôt

```
PIL1_2526_16/
├── README.md                      ← Ce fichier
├── rapport.html                   ← Rapport de projet en HTML
├── schema.sql                     ← Structure finale de la base de données
└── frontend/
    ├── pages/
    │   ├── index.html             ← Page d'accueil
    │   ├── login.html             ← Connexion
    │   ├── register.html          ← Inscription
    │   ├── profil.html            ← Profil utilisateur
    │   ├── matching.html          ← Mise en correspondance
    │   └── chat.html              ← Messagerie
    ├── css/
    │   ├── base.css
    │   ├── buttons.css
    │   ├── navbar.css
    │   ├── forms.css
    │   ├── cards.css
    │   ├── auth.css
    │   ├── hero.css
    │   ├── profil.css
    │   ├── matching.css
    │   └── chat.css
    └── assets/
        ├── images/
        └── icons/
```

---

## 6. Base de données

Le fichier `schema.sql` contient la structure complète de la base de données MySQL/PostgreSQL.

### Tables principales

| Table | Description |
|---|---|
| `utilisateurs` | Comptes et informations personnelles |
| `profils` | Compétences, filière, niveau, bio, disponibilités |
| `competences` | Liste des matières et compétences disponibles |
| `offres_mentorat` | Offres et demandes publiées |
| `matchs` | Résultats de correspondance avec scores |
| `conversations` | Sessions de messagerie entre utilisateurs |
| `messages` | Messages échangés dans chaque conversation |

---

## 7. Instructions de déploiement

### Prérequis

- Python 3.10+
- pip
- MySQL ou PostgreSQL
- Git

### Étapes

**1. Cloner le dépôt**
```bash
git clone https://github.com/PIL1-2526-16/PIL1_2526_16.git
cd PIL1_2526_16
```

**2. Créer et activer l'environnement virtuel**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

**3. Installer les dépendances**
```bash
pip install -r requirements.txt
```

**4. Configurer la base de données**
```bash
# Créer la base de données puis importer le schéma
mysql -u root -p mentorlink < schema.sql
```

**5. Configurer les variables d'environnement**

Créer un fichier `.env` à la racine :
```
DB_NAME=mentorlink
DB_USER=root
DB_PASSWORD=ton_mot_de_passe
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=ta_cle_secrete
```

**6. Lancer le serveur**
```bash
python manage.py migrate
python manage.py runserver
```

**7. Accéder à l'application**

Ouvrir le navigateur sur : `http://127.0.0.1:8000`

---

## 8. Manuel d'utilisation

### Créer un compte

1. Accéder à la page d'accueil
2. Cliquer sur **S'inscrire**
3. Remplir le formulaire : nom, prénom, email, téléphone, filière, niveau, mot de passe
4. Sélectionner ses points forts et points faibles
5. Valider l'inscription

### Se connecter

1. Cliquer sur **Connexion**
2. Saisir son email ou numéro de téléphone et son mot de passe
3. Cliquer sur **Se connecter**

### Trouver un mentor

1. Aller dans l'onglet **Matching**
2. Consulter les résultats proposés automatiquement par l'algorithme
3. Filtrer par matière, format (en ligne / présentiel) ou disponibilité
4. Cliquer sur **Contacter** pour envoyer un message

### Publier une offre ou demande de mentorat

1. Dans la page **Matching**, cliquer sur **Publier une offre** ou **Publier une demande**
2. Renseigner les matières concernées, les disponibilités et le format souhaité
3. Valider la publication

### Utiliser la messagerie

1. Aller dans l'onglet **Messages**
2. Sélectionner une conversation dans la liste à gauche
3. Saisir un message dans le champ en bas et appuyer sur **Entrée** ou cliquer sur le bouton d'envoi

### Modifier son profil

1. Aller dans l'onglet **Profil**
2. Cliquer sur **Modifier** dans la section souhaitée (bio, compétences, disponibilités)
3. Sauvegarder les modifications

---

## 9. Technologies utilisées

| Couche | Technologie |
|---|---|
| **Frontend** | HTML5 sémantique, CSS3 modulaire, JavaScript |
| **Framework CSS** | Bootstrap 5.3 |
| **Backend** | Python 3, Django |
| **Base de données** | MySQL / PostgreSQL |
| **Versioning** | Git & GitHub |
| **Police** | Poppins (Google Fonts) |
| **Icônes** | Bootstrap Icons |

---

## Encadrement

| Rôle | Nom |
|---|---|
| Supervision | M. Ratheil HOUNDJI |
| Encadrant | M. Armand ACCROMBESSI |
| Encadrante | Mme Maryse GAHOU |

---

*IFRI — Université d'Abomey-Calavi — Projet Intégrateur L1 2025-2026 — Groupe PIL1_2526_16*

