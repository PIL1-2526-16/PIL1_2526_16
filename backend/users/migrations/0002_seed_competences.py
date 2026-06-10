from django.db import migrations


CATEGORIES = [
    'Mathématiques & Sciences fondamentales',
    'Programmation',
    'Réseaux & Systèmes',
    'Bases de données',
    'Sécurité Informatique',
    'Génie Logiciel & Qualité',
    'Intelligence Artificielle & Data',
    'Web & Infographie',
    'Gestion & Méthodologie',
    'Culture générale & Transversal',
]

COMPETENCES = {
    'Mathématiques & Sciences fondamentales': [
        'Logique, arithmétique et applications',
        'Algèbre linéaire et applications',
        'Probabilités, statistiques et analyse combinatoire',
        'Équations différentielles et calcul intégral',
        'Suites et séries numériques',
        'Mathématiques pour informatique (niveau Master)',
        'Statistiques et probabilités pour la science des données',
    ],
    'Programmation': [
        'Algorithmique et langage C',
        'Programmation Python',
        'Programmation orientée objet (Java, C++)',
        'Structures de données et applications (C/Python)',
        'Programmation avancée (Java, Python, R)',
        'Programmation graphique (Qt/C++)',
    ],
    'Réseaux & Systèmes': [
        'Architecture et topologie des réseaux',
        "Systèmes d'exploitation (Windows/Linux)",
        'Administration systèmes et réseaux',
        'Ingénierie des réseaux (CISCO CCNA)',
        'Routage WAN, commutation',
        'Réseaux sans fil et IoT (RCSF)',
        'Systèmes répartis, embarqués et temps réel',
        'Technologies Cloud (Kubernetes, Serverless)',
    ],
    'Bases de données': [
        'SGBD et langage SQL',
        'Bases de données relationnelles et NoSQL',
        'Bases de données avancées',
        'Big Data (bases et outils)',
        'Administration BDD (Oracle, PostgreSQL)',
        'Bases de données distribuées',
        'BDD multimédia et web sémantique',
    ],
    'Sécurité Informatique': [
        'Politique de sécurité des SI',
        'Sécurité des réseaux (WEP, WPA, WPS, BAS)',
        'Cryptographie et applications',
        'Sécurité Web et Mobile (OWASP)',
        'Audit et normes de sécurité',
        'Management de la sécurité du SI',
        'Sécurité des applications et reverse engineering',
        'DevSecOps',
        'Blockchain et applications',
    ],
    'Génie Logiciel & Qualité': [
        'Bases du génie logiciel',
        'Méthode Agile Scrum',
        'Assurance qualité et test logiciel',
        "Cycle de vie d'un logiciel",
        'Fiabilité et sécurité logicielle',
        'Génie logiciel et PGI/ERP',
    ],
    'Intelligence Artificielle & Data': [
        "Concepts et applications de l'IA",
        'Apprentissage automatique (supervisé/non supervisé)',
        'Réseaux de neurones artificiels',
        'Data Mining',
        "Traitement du signal et d'image",
        'Outils cloud pour la data science',
        'Techniques de résolution par la recherche',
    ],
    'Web & Infographie': [
        'Technologies web avancées',
        'Développement web (HTML, CSS, frameworks)',
        'Technologies mobiles avancées',
        'Infographie et développement web appliqué',
    ],
    'Gestion & Méthodologie': [
        'Gestion de projets informatiques',
        "Méthodes d'analyse et de conception (UML, Merise)",
        'Méthodologie de rédaction de mémoire',
        'Recherche opérationnelle',
        'Interfaces homme-machine',
        "Entrepreneuriat et plan d'affaires",
        'Stage et discipline',
    ],
    'Culture générale & Transversal': [
        'Anglais technique et communication scientifique',
        'Communication managériale',
        'Déontologie et droit lié aux TIC',
        "Techniques d'expression écrite et orale",
        'Maintenance des appareils électroniques',
    ],
}


def seed(apps, schema_editor):
    Categorie = apps.get_model('users', 'Categorie')
    Competence = apps.get_model('users', 'Competence')

    for nom_categorie in CATEGORIES:
        categorie, _ = Categorie.objects.get_or_create(nom_categorie=nom_categorie)
        for nom_competence in COMPETENCES[nom_categorie]:
            Competence.objects.get_or_create(categorie=categorie, nom_competence=nom_competence)


def unseed(apps, schema_editor):
    Categorie = apps.get_model('users', 'Categorie')
    Categorie.objects.filter(nom_categorie__in=CATEGORIES).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
