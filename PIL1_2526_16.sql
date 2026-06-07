-- ============================================================
-- IFRI_MentorLink — Structure de la base de données
-- Groupe : 16
-- ============================================================

CREATE DATABASE IF NOT EXISTS ifri_mentorlink
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE ifri_mentorlink;


CREATE TABLE UTILISATEUR (
    id_utilisateur  INT             NOT NULL AUTO_INCREMENT,
    nom             VARCHAR(50)     NOT NULL,
    prenom          VARCHAR(50)     NOT NULL,
    email           VARCHAR(100)    NOT NULL,
    telephone       VARCHAR(20)     NOT NULL,
    mot_de_passe    VARCHAR(255)    NOT NULL,
    photo_profil    VARCHAR(255)    DEFAULT NULL,
    filiere         ENUM('IA', 'IM', 'GL', 'SE&IoT', 'SI') NOT NULL,
    niveau          ENUM('L1', 'L2', 'L3')                 NOT NULL,
    bio             TEXT            DEFAULT NULL,
    centres_interet TEXT            DEFAULT NULL,
    date_inscription DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id_utilisateur),
    UNIQUE KEY uq_email     (email),
    UNIQUE KEY uq_telephone (telephone)
);


CREATE TABLE CATEGORIE (
    id_categorie   INT          NOT NULL AUTO_INCREMENT,
    nom_categorie  VARCHAR(100) NOT NULL,
 
    PRIMARY KEY (id_categorie),
    UNIQUE KEY uq_nom_categorie (nom_categorie)
);


CREATE TABLE COMPETENCE (
    id_competence  INT          NOT NULL AUTO_INCREMENT,
    id_categorie   INT          NOT NULL,
    nom_competence VARCHAR(150) NOT NULL,
 
    PRIMARY KEY (id_competence),
    UNIQUE KEY uq_nom_competence (nom_competence),
 
    CONSTRAINT fk_comp_categorie
        FOREIGN KEY (id_categorie)
        REFERENCES CATEGORIE (id_categorie)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE UTILISATEUR_COMPETENCE (
    id_util_comp    INT             NOT NULL AUTO_INCREMENT,
    id_utilisateur  INT             NOT NULL,
    id_competence   INT             NOT NULL,
    type_competence ENUM('point_fort', 'point_faible') NOT NULL,

    PRIMARY KEY (id_util_comp),
    UNIQUE KEY uq_util_comp (id_utilisateur, id_competence, type_competence),

    CONSTRAINT fk_uc_utilisateur
        FOREIGN KEY (id_utilisateur)
        REFERENCES UTILISATEUR (id_utilisateur)
        ON DELETE CASCADE ON UPDATE CASCADE,              /* Suppression en cascade et mise à jour en cascade */

    CONSTRAINT fk_uc_competence
        FOREIGN KEY (id_competence)
        REFERENCES COMPETENCE (id_competence)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE DISPONIBILITE (
    id_disponibilite INT            NOT NULL AUTO_INCREMENT,
    id_utilisateur   INT            NOT NULL,
    jour             ENUM('Lundi', 'Mardi', 'Mercredi', 'Jeudi',
                          'Vendredi', 'Samedi', 'Dimanche') NOT NULL,
    heure_debut      TIME           NOT NULL,
    heure_fin        TIME           NOT NULL,

    PRIMARY KEY (id_disponibilite),

    CONSTRAINT fk_dispo_utilisateur
        FOREIGN KEY (id_utilisateur)
        REFERENCES UTILISATEUR (id_utilisateur)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE OFFRE_MENTORAT (
    id_offre         INT            NOT NULL AUTO_INCREMENT,
    id_utilisateur   INT            NOT NULL,
    id_competence    INT            NOT NULL,
    type_offre       ENUM('offre', 'demande')                        NOT NULL,
    format           ENUM('présentiel', 'en ligne', 'les deux')      NOT NULL,
    statut           ENUM('ouverte', 'fermée')                       NOT NULL DEFAULT 'ouverte',
    date_publication DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id_offre),

    CONSTRAINT fk_offre_utilisateur
        FOREIGN KEY (id_utilisateur)
        REFERENCES UTILISATEUR (id_utilisateur)
        ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_offre_competence
        FOREIGN KEY (id_competence)
        REFERENCES COMPETENCE (id_competence)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE MATCHING (
    id_matching     INT             NOT NULL AUTO_INCREMENT,
    id_mentor       INT             NOT NULL,
    id_mentore      INT             NOT NULL,
    id_offre        INT             NOT NULL,
    score           DECIMAL(5, 2)   NOT NULL,                       /* Score du matching, décimal sur 5 caractères dont 2 décimaux */
    statut          ENUM('proposé', 'accepté', 'refusé') NOT NULL DEFAULT 'proposé',
    date_matching   DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id_matching),

    CONSTRAINT chk_score
        CHECK (score BETWEEN 0 AND 100),                 /* Le score doit être compris entre 0 et 100 */

    CONSTRAINT chk_mentor_mentore
        CHECK (id_mentor <> id_mentore),                      /* Un mentor ne peut pas être son propre mentore */

    CONSTRAINT fk_matching_mentor
        FOREIGN KEY (id_mentor)
        REFERENCES UTILISATEUR (id_utilisateur)
        ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_matching_mentore
        FOREIGN KEY (id_mentore)
        REFERENCES UTILISATEUR (id_utilisateur)
        ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_matching_offre
        FOREIGN KEY (id_offre)
        REFERENCES OFFRE_MENTORAT (id_offre)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE CONVERSATION (
    id_conversation  INT            NOT NULL AUTO_INCREMENT,
    id_utilisateur1  INT            NOT NULL,
    id_utilisateur2  INT            NOT NULL,
    date_creation    DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id_conversation),
    UNIQUE KEY uq_conversation (id_utilisateur1, id_utilisateur2),

    CONSTRAINT chk_participants
        CHECK (id_utilisateur1 <> id_utilisateur2),

    CONSTRAINT fk_conv_utilisateur1
        FOREIGN KEY (id_utilisateur1)
        REFERENCES UTILISATEUR (id_utilisateur)
        ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_conv_utilisateur2
        FOREIGN KEY (id_utilisateur2)
        REFERENCES UTILISATEUR (id_utilisateur)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE MESSAGE (
    id_message       INT            NOT NULL AUTO_INCREMENT,
    id_conversation  INT            NOT NULL,
    id_expediteur    INT            NOT NULL,
    contenu          TEXT           NOT NULL,
    date_envoi       DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    lu               BOOLEAN        NOT NULL DEFAULT FALSE,

    PRIMARY KEY (id_message),

    CONSTRAINT fk_message_conversation
        FOREIGN KEY (id_conversation)
        REFERENCES CONVERSATION (id_conversation)
        ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_message_expediteur
        FOREIGN KEY (id_expediteur)
        REFERENCES UTILISATEUR (id_utilisateur)
        ON DELETE CASCADE ON UPDATE CASCADE
);


INSERT INTO CATEGORIE (nom_categorie) VALUES         /* Données de la table CATEGORIE */
    ('Mathématiques & Sciences fondamentales'),
    ('Programmation'),
    ('Réseaux & Systèmes'),
    ('Bases de données'),
    ('Sécurité Informatique'),
    ('Génie Logiciel & Qualité'),
    ('Intelligence Artificielle & Data'),
    ('Web & Infographie'),
    ('Gestion & Méthodologie'),
    ('Culture générale & Transversal');


INSERT INTO COMPETENCE (id_categorie, nom_competence) VALUES            /* Données de la table COMPETENCE de la catégorie 'Mathématiques & Sciences fondamentales'*/
    (1, 'Logique, arithmétique et applications'),
    (1, 'Algèbre linéaire et applications'),
    (1, 'Probabilités, statistiques et analyse combinatoire'),
    (1, 'Équations différentielles et calcul intégral'),
    (1, 'Suites et séries numériques'),
    (1, 'Mathématiques pour informatique (niveau Master)'),
    (1, 'Statistiques et probabilités pour la science des données');


INSERT INTO COMPETENCE (id_categorie, nom_competence) VALUES                    /* Données de la table COMPETENCE de la catégorie 'Programmation'*/
    (2, 'Algorithmique et langage C'),
    (2, 'Programmation Python'),
    (2, 'Programmation orientée objet (Java, C++)'),
    (2, 'Structures de données et applications (C/Python)'),
    (2, 'Programmation avancée (Java, Python, R)'),
    (2, 'Programmation graphique (Qt/C++)');


INSERT INTO COMPETENCE (id_categorie, nom_competence) VALUES                /* Données de la table COMPETENCE de la catégorie 'Réseaux & Systèmes'*/
    (3, 'Architecture et topologie des réseaux'),
    (3, "Systèmes d'exploitation (Windows/Linux)"),
    (3, 'Administration systèmes et réseaux'),
    (3, 'Ingénierie des réseaux (CISCO CCNA)'),
    (3, 'Routage WAN, commutation'),
    (3, 'Réseaux sans fil et IoT (RCSF)'),
    (3, 'Systèmes répartis, embarqués et temps réel'),
    (3, 'Technologies Cloud (Kubernetes, Serverless)');


INSERT INTO COMPETENCE (id_categorie, nom_competence) VALUES                  /* Données de la table COMPETENCE de la catégorie 'Bases de données'*/
    (4, 'SGBD et langage SQL'),
    (4, 'Bases de données relationnelles et NoSQL'),
    (4, 'Bases de données avancées'),
    (4, 'Big Data (bases et outils)'),
    (4, 'Administration BDD (Oracle, PostgreSQL)'),
    (4, 'Bases de données distribuées'),
    (4, 'BDD multimédia et web sémantique');


INSERT INTO COMPETENCE (id_categorie, nom_competence) VALUES                 /* Données de la table COMPETENCE de la catégorie 'Sécurité Informatique'*/
    (5, 'Politique de sécurité des SI'),
    (5, 'Sécurité des réseaux (WEP, WPA, WPS, BAS)'),
    (5, 'Cryptographie et applications'),
    (5, 'Sécurité Web et Mobile (OWASP)'),
    (5, 'Audit et normes de sécurité'),
    (5, 'Management de la sécurité du SI'),
    (5, 'Sécurité des applications et reverse engineering'),
    (5, 'DevSecOps'),
    (5, 'Blockchain et applications');


INSERT INTO COMPETENCE (id_categorie, nom_competence) VALUES                   /* Données de la table COMPETENCE de la catégorie 'Génie Logiciel & Qualité'*/
    (6, 'Bases du génie logiciel'),
    (6, 'Méthode Agile Scrum'),
    (6, 'Assurance qualité et test logiciel'),
    (6, "Cycle de vie d'un logiciel"),
    (6, 'Fiabilité et sécurité logicielle'),
    (6, 'Génie logiciel et PGI/ERP');


INSERT INTO COMPETENCE (id_categorie, nom_competence) VALUES                    /* Données de la table COMPETENCE de la catégorie 'Intelligence Artificielle & Data'*/
    (7, "Concepts et applications de l'IA"),
    (7, 'Apprentissage automatique (supervisé/non supervisé)'),
    (7, 'Réseaux de neurones artificiels'),
    (7, 'Data Mining'),
    (7, "Traitement du signal et d'image"),
    (7, 'Outils cloud pour la data science'),
    (7, 'Techniques de résolution par la recherche');


INSERT INTO COMPETENCE (id_categorie, nom_competence) VALUES                   /* Données de la table COMPETENCE de la catégorie 'Web & Infographie'*/
    (8, 'Technologies web avancées'),
    (8, 'Développement web (HTML, CSS, frameworks)'),
    (8, 'Technologies mobiles avancées'),
    (8, 'Infographie et développement web appliqué');


INSERT INTO COMPETENCE (id_categorie, nom_competence) VALUES                   /* Données de la table COMPETENCE de la catégorie 'Gestion & Méthodologie'*/
    (9, 'Gestion de projets informatiques'),
    (9, "Méthodes d'analyse et de conception (UML, Merise)"),
    (9, 'Méthodologie de rédaction de mémoire'),
    (9, 'Recherche opérationnelle'),
    (9, 'Interfaces homme-machine'),
    (9, "Entrepreneuriat et plan d'affaires"),
    (9, 'Stage et discipline');


INSERT INTO COMPETENCE (id_categorie, nom_competence) VALUES                   /* Données de la table COMPETENCE de la catégorie 'Culture générale & Transversal'*/
    (10, 'Anglais technique et communication scientifique'),
    (10, 'Communication managériale'),
    (10, 'Déontologie et droit lié aux TIC'),
    (10, "Techniques d'expression écrite et orale"),
    (10, 'Maintenance des appareils électroniques');


SELECT * FROM CATEGORIE;          /* Affiche les données de la table CATEGORIE */
