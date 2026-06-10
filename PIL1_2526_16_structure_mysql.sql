-- ============================================================
-- IFRI_MentorLink — Structure de la base de données (MySQL)
-- Générée depuis les migrations Django (manage.py migrate)
-- Base : ifri_mentorlink
-- ============================================================

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_utilisateur_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_utilisateur_id` FOREIGN KEY (`user_id`) REFERENCES `users_utilisateur` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `matching_matching`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matching_matching` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `score` decimal(5,2) NOT NULL,
  `statut` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_matching` datetime(6) NOT NULL,
  `mentor_id` bigint NOT NULL,
  `mentore_id` bigint NOT NULL,
  `offre_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `matching_matching_mentor_id_55b626be_fk_users_utilisateur_id` (`mentor_id`),
  KEY `matching_matching_mentore_id_5061f29b_fk_users_utilisateur_id` (`mentore_id`),
  KEY `matching_matching_offre_id_e68709f5_fk_matching_offrementorat_id` (`offre_id`),
  CONSTRAINT `matching_matching_mentor_id_55b626be_fk_users_utilisateur_id` FOREIGN KEY (`mentor_id`) REFERENCES `users_utilisateur` (`id`),
  CONSTRAINT `matching_matching_mentore_id_5061f29b_fk_users_utilisateur_id` FOREIGN KEY (`mentore_id`) REFERENCES `users_utilisateur` (`id`),
  CONSTRAINT `matching_matching_offre_id_e68709f5_fk_matching_offrementorat_id` FOREIGN KEY (`offre_id`) REFERENCES `matching_offrementorat` (`id`),
  CONSTRAINT `mentor_diff_mentore` CHECK ((`mentor_id` <> `mentore_id`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `matching_offrementorat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matching_offrementorat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type_offre` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `format` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  `statut` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_publication` datetime(6) NOT NULL,
  `competence_id` bigint NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `matching_offrementor_competence_id_544cbe68_fk_users_com` (`competence_id`),
  KEY `matching_offrementor_utilisateur_id_22566378_fk_users_uti` (`utilisateur_id`),
  CONSTRAINT `matching_offrementor_competence_id_544cbe68_fk_users_com` FOREIGN KEY (`competence_id`) REFERENCES `users_competence` (`id`),
  CONSTRAINT `matching_offrementor_utilisateur_id_22566378_fk_users_uti` FOREIGN KEY (`utilisateur_id`) REFERENCES `users_utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `messaging_conversation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messaging_conversation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_creation` datetime(6) NOT NULL,
  `utilisateur1_id` bigint NOT NULL,
  `utilisateur2_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `messaging_conversation_utilisateur1_id_utilisat_3cb7e3cd_uniq` (`utilisateur1_id`,`utilisateur2_id`),
  KEY `messaging_conversati_utilisateur2_id_09fee226_fk_users_uti` (`utilisateur2_id`),
  CONSTRAINT `messaging_conversati_utilisateur1_id_2654d660_fk_users_uti` FOREIGN KEY (`utilisateur1_id`) REFERENCES `users_utilisateur` (`id`),
  CONSTRAINT `messaging_conversati_utilisateur2_id_09fee226_fk_users_uti` FOREIGN KEY (`utilisateur2_id`) REFERENCES `users_utilisateur` (`id`),
  CONSTRAINT `participants_differents` CHECK ((`utilisateur1_id` <> `utilisateur2_id`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `messaging_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messaging_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `contenu` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_envoi` datetime(6) NOT NULL,
  `lu` tinyint(1) NOT NULL,
  `conversation_id` bigint NOT NULL,
  `expediteur_id` bigint NOT NULL,
  `fichier` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `messaging_message_conversation_id_3db4d3d1_fk_messaging` (`conversation_id`),
  KEY `messaging_message_expediteur_id_2474964f_fk_users_utilisateur_id` (`expediteur_id`),
  CONSTRAINT `messaging_message_conversation_id_3db4d3d1_fk_messaging` FOREIGN KEY (`conversation_id`) REFERENCES `messaging_conversation` (`id`),
  CONSTRAINT `messaging_message_expediteur_id_2474964f_fk_users_utilisateur_id` FOREIGN KEY (`expediteur_id`) REFERENCES `users_utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `users_categorie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_categorie` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom_categorie` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nom_categorie` (`nom_categorie`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

-- Données de référence : catégories de compétences
LOCK TABLES `users_categorie` WRITE;
/*!40000 ALTER TABLE `users_categorie` DISABLE KEYS */;
INSERT INTO `users_categorie` (`id`, `nom_categorie`) VALUES (4,'Bases de données'),(10,'Culture générale & Transversal'),(6,'Génie Logiciel & Qualité'),(9,'Gestion & Méthodologie'),(7,'Intelligence Artificielle & Data'),(1,'Mathématiques & Sciences fondamentales'),(2,'Programmation'),(3,'Réseaux & Systèmes'),(5,'Sécurité Informatique'),(8,'Web & Infographie');
/*!40000 ALTER TABLE `users_categorie` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `users_competence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_competence` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom_competence` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `categorie_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nom_competence` (`nom_competence`),
  KEY `users_competence_categorie_id_8a56f846_fk_users_categorie_id` (`categorie_id`),
  CONSTRAINT `users_competence_categorie_id_8a56f846_fk_users_categorie_id` FOREIGN KEY (`categorie_id`) REFERENCES `users_categorie` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

-- Données de référence : compétences (66 compétences réparties dans les 10 catégories)
LOCK TABLES `users_competence` WRITE;
/*!40000 ALTER TABLE `users_competence` DISABLE KEYS */;
INSERT INTO `users_competence` (`id`, `nom_competence`, `categorie_id`) VALUES (1,'Logique, arithmétique et applications',1),(2,'Algèbre linéaire et applications',1),(3,'Probabilités, statistiques et analyse combinatoire',1),(4,'Équations différentielles et calcul intégral',1),(5,'Suites et séries numériques',1),(6,'Mathématiques pour informatique (niveau Master)',1),(7,'Statistiques et probabilités pour la science des données',1),(8,'Algorithmique et langage C',2),(9,'Programmation Python',2),(10,'Programmation orientée objet (Java, C++)',2),(11,'Structures de données et applications (C/Python)',2),(12,'Programmation avancée (Java, Python, R)',2),(13,'Programmation graphique (Qt/C++)',2),(14,'Architecture et topologie des réseaux',3),(15,'Systèmes d\'exploitation (Windows/Linux)',3),(16,'Administration systèmes et réseaux',3),(17,'Ingénierie des réseaux (CISCO CCNA)',3),(18,'Routage WAN, commutation',3),(19,'Réseaux sans fil et IoT (RCSF)',3),(20,'Systèmes répartis, embarqués et temps réel',3),(21,'Technologies Cloud (Kubernetes, Serverless)',3),(22,'SGBD et langage SQL',4),(23,'Bases de données relationnelles et NoSQL',4),(24,'Bases de données avancées',4),(25,'Big Data (bases et outils)',4),(26,'Administration BDD (Oracle, PostgreSQL)',4),(27,'Bases de données distribuées',4),(28,'BDD multimédia et web sémantique',4),(29,'Politique de sécurité des SI',5),(30,'Sécurité des réseaux (WEP, WPA, WPS, BAS)',5),(31,'Cryptographie et applications',5),(32,'Sécurité Web et Mobile (OWASP)',5),(33,'Audit et normes de sécurité',5),(34,'Management de la sécurité du SI',5),(35,'Sécurité des applications et reverse engineering',5),(36,'DevSecOps',5),(37,'Blockchain et applications',5),(38,'Bases du génie logiciel',6),(39,'Méthode Agile Scrum',6),(40,'Assurance qualité et test logiciel',6),(41,'Cycle de vie d\'un logiciel',6),(42,'Fiabilité et sécurité logicielle',6),(43,'Génie logiciel et PGI/ERP',6),(44,'Concepts et applications de l\'IA',7),(45,'Apprentissage automatique (supervisé/non supervisé)',7),(46,'Réseaux de neurones artificiels',7),(47,'Data Mining',7),(48,'Traitement du signal et d\'image',7),(49,'Outils cloud pour la data science',7),(50,'Techniques de résolution par la recherche',7),(51,'Technologies web avancées',8),(52,'Développement web (HTML, CSS, frameworks)',8),(53,'Technologies mobiles avancées',8),(54,'Infographie et développement web appliqué',8),(55,'Gestion de projets informatiques',9),(56,'Méthodes d\'analyse et de conception (UML, Merise)',9),(57,'Méthodologie de rédaction de mémoire',9),(58,'Recherche opérationnelle',9),(59,'Interfaces homme-machine',9),(60,'Entrepreneuriat et plan d\'affaires',9),(61,'Stage et discipline',9),(62,'Anglais technique et communication scientifique',10),(63,'Communication managériale',10),(64,'Déontologie et droit lié aux TIC',10),(65,'Techniques d\'expression écrite et orale',10),(66,'Maintenance des appareils électroniques',10);
/*!40000 ALTER TABLE `users_competence` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `users_disponibilite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_disponibilite` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `jour` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `heure_debut` time(6) NOT NULL,
  `heure_fin` time(6) NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_disponibilite_utilisateur_id_abc4d75a_fk_users_uti` (`utilisateur_id`),
  CONSTRAINT `users_disponibilite_utilisateur_id_abc4d75a_fk_users_uti` FOREIGN KEY (`utilisateur_id`) REFERENCES `users_utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `users_utilisateur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_utilisateur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `nom` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `prenom` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `telephone` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `photo_profil` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `filiere` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `niveau` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `bio` longtext COLLATE utf8mb4_unicode_ci,
  `centres_interet` longtext COLLATE utf8mb4_unicode_ci,
  `date_inscription` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `telephone` (`telephone`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `users_utilisateur_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_utilisateur_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `utilisateur_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_utilisateur_groups_utilisateur_id_group_id_753c4b93_uniq` (`utilisateur_id`,`group_id`),
  KEY `users_utilisateur_groups_group_id_a71698e9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_utilisateur_gr_utilisateur_id_a9ec7e2b_fk_users_uti` FOREIGN KEY (`utilisateur_id`) REFERENCES `users_utilisateur` (`id`),
  CONSTRAINT `users_utilisateur_groups_group_id_a71698e9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `users_utilisateur_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_utilisateur_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `utilisateur_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_utilisateur_user_p_utilisateur_id_permissio_76fca242_uniq` (`utilisateur_id`,`permission_id`),
  KEY `users_utilisateur_us_permission_id_c32f2ac3_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_utilisateur_us_permission_id_c32f2ac3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_utilisateur_us_utilisateur_id_fce4c46b_fk_users_uti` FOREIGN KEY (`utilisateur_id`) REFERENCES `users_utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `users_utilisateurcompetence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_utilisateurcompetence` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type_competence` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `competence_id` bigint NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_utilisateurcompete_utilisateur_id_competenc_af28ec7b_uniq` (`utilisateur_id`,`competence_id`,`type_competence`),
  KEY `users_utilisateurcom_competence_id_3ccbe0a7_fk_users_com` (`competence_id`),
  CONSTRAINT `users_utilisateurcom_competence_id_3ccbe0a7_fk_users_com` FOREIGN KEY (`competence_id`) REFERENCES `users_competence` (`id`),
  CONSTRAINT `users_utilisateurcom_utilisateur_id_592cdd40_fk_users_uti` FOREIGN KEY (`utilisateur_id`) REFERENCES `users_utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

