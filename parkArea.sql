CREATE DATABASE  IF NOT EXISTS `parkArea` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `parkArea`;
-- MySQL dump 10.13  Distrib 5.7.30, for Linux (x86_64)
--
-- Host: localhost    Database: parkArea
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add location',1,'add_location'),(2,'Can change location',1,'change_location'),(3,'Can delete location',1,'delete_location'),(4,'Can view location',1,'view_location'),(5,'Can add district',2,'add_district'),(6,'Can change district',2,'change_district'),(7,'Can delete district',2,'delete_district'),(8,'Can view district',2,'view_district'),(9,'Can add province',3,'add_province'),(10,'Can change province',3,'change_province'),(11,'Can delete province',3,'delete_province'),(12,'Can view province',3,'view_province'),(13,'Can add region',4,'add_region'),(14,'Can change region',4,'change_region'),(15,'Can delete region',4,'delete_region'),(16,'Can view region',4,'view_region'),(17,'Can add geography',5,'add_geography'),(18,'Can change geography',5,'change_geography'),(19,'Can delete geography',5,'delete_geography'),(20,'Can view geography',5,'view_geography'),(21,'Can add person',6,'add_person'),(22,'Can change person',6,'change_person'),(23,'Can delete person',6,'delete_person'),(24,'Can view person',6,'view_person'),(25,'Can add identifier',7,'add_identifier'),(26,'Can change identifier',7,'change_identifier'),(27,'Can delete identifier',7,'delete_identifier'),(28,'Can view identifier',7,'view_identifier'),(29,'Can add actor',8,'add_actor'),(30,'Can change actor',8,'change_actor'),(31,'Can delete actor',8,'delete_actor'),(32,'Can view actor',8,'view_actor'),(33,'Can add specie',9,'add_specie'),(34,'Can change specie',9,'change_specie'),(35,'Can delete specie',9,'delete_specie'),(36,'Can view specie',9,'view_specie'),(37,'Can add genero',10,'add_genero'),(38,'Can change genero',10,'change_genero'),(39,'Can delete genero',10,'delete_genero'),(40,'Can view genero',10,'view_genero'),(41,'Can add ordem',11,'add_ordem'),(42,'Can change ordem',11,'change_ordem'),(43,'Can delete ordem',11,'delete_ordem'),(44,'Can view ordem',11,'view_ordem'),(45,'Can add familia',12,'add_familia'),(46,'Can change familia',12,'change_familia'),(47,'Can delete familia',12,'delete_familia'),(48,'Can view familia',12,'view_familia'),(49,'Can add classe',13,'add_classe'),(50,'Can change classe',13,'change_classe'),(51,'Can delete classe',13,'delete_classe'),(52,'Can view classe',13,'view_classe'),(53,'Can add filo',14,'add_filo'),(54,'Can change filo',14,'change_filo'),(55,'Can delete filo',14,'delete_filo'),(56,'Can view filo',14,'view_filo'),(57,'Can add reino',15,'add_reino'),(58,'Can change reino',15,'change_reino'),(59,'Can delete reino',15,'delete_reino'),(60,'Can view reino',15,'view_reino'),(61,'Can add log entry',16,'add_logentry'),(62,'Can change log entry',16,'change_logentry'),(63,'Can delete log entry',16,'delete_logentry'),(64,'Can view log entry',16,'view_logentry'),(65,'Can add permission',17,'add_permission'),(66,'Can change permission',17,'change_permission'),(67,'Can delete permission',17,'delete_permission'),(68,'Can view permission',17,'view_permission'),(69,'Can add group',18,'add_group'),(70,'Can change group',18,'change_group'),(71,'Can delete group',18,'delete_group'),(72,'Can view group',18,'view_group'),(73,'Can add user',19,'add_user'),(74,'Can change user',19,'change_user'),(75,'Can delete user',19,'delete_user'),(76,'Can view user',19,'view_user'),(77,'Can add content type',20,'add_contenttype'),(78,'Can change content type',20,'change_contenttype'),(79,'Can delete content type',20,'delete_contenttype'),(80,'Can view content type',20,'view_contenttype'),(81,'Can add session',21,'add_session'),(82,'Can change session',21,'change_session'),(83,'Can delete session',21,'delete_session'),(84,'Can view session',21,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$PEQexO2kdmAK$UXB/ITt62sdS6CtFoQhPQrFUP5ZYhkoxVndq/DAalrY=','2020-07-25 10:14:09.983396',1,'digio','','','guerzeneldo@gmail.com',1,1,'2020-07-18 21:39:58.440524'),(2,'pbkdf2_sha256$150000$Bkc1pouVpnvE$UnICPVMSYlP9/qHL7HTClkHsfjigDgaI/mwPZs65fnA=','2020-07-24 18:46:39.507047',0,'rofino','Rofino','Chunga','rchunga@gmail.com',1,1,'2020-07-24 18:44:43.000000'),(3,'pbkdf2_sha256$150000$8A1eyMH2Qr3H$1xeLK0/HLQgDfjMP8iiBcHB22r1z1d2DhcQyocZq5Os=','2020-07-25 10:25:48.000000',0,'Dalton','Dalton','Mirasse','dmirasse@kenmaremoz.com',0,1,'2020-07-25 10:24:02.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (1,2,33),(2,2,36),(4,3,33),(5,3,34),(6,3,35),(7,3,36),(3,3,65),(8,3,70),(9,3,71),(10,3,72);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classe`
--

DROP TABLE IF EXISTS `classe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classe` (
  `idclasse` int(11) NOT NULL AUTO_INCREMENT,
  `classe` varchar(200) DEFAULT NULL,
  `idfilo` int(11) DEFAULT NULL,
  PRIMARY KEY (`idclasse`),
  KEY `fk_classe_1_idx` (`idfilo`),
  CONSTRAINT `fk_classe_1` FOREIGN KEY (`idfilo`) REFERENCES `filo` (`idfilo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classe`
--

LOCK TABLES `classe` WRITE;
/*!40000 ALTER TABLE `classe` DISABLE KEYS */;
/*!40000 ALTER TABLE `classe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distrito`
--

DROP TABLE IF EXISTS `distrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `distrito` (
  `iddistrito` int(11) NOT NULL AUTO_INCREMENT,
  `distrito` varchar(45) DEFAULT NULL,
  `idprovincia` int(11) DEFAULT NULL,
  PRIMARY KEY (`iddistrito`),
  KEY `fk_distrito_1_idx` (`idprovincia`),
  CONSTRAINT `fk_distrito_1` FOREIGN KEY (`idprovincia`) REFERENCES `provincia` (`idprovincia`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distrito`
--

LOCK TABLES `distrito` WRITE;
/*!40000 ALTER TABLE `distrito` DISABLE KEYS */;
/*!40000 ALTER TABLE `distrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-07-24 18:44:43.899904','2','rofino',1,'[{\"added\": {}}]',19,1),(2,'2020-07-24 18:46:31.212908','2','rofino',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"is_staff\", \"user_permissions\"]}}]',19,1),(3,'2020-07-24 18:47:18.479128','1','FD',1,'[{\"added\": {}}]',9,2),(4,'2020-07-25 10:24:02.817428','3','Dalton',1,'[{\"added\": {}}]',19,1),(5,'2020-07-25 10:25:51.252050','3','Dalton',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"user_permissions\", \"last_login\"]}}]',19,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'actor','actor'),(16,'admin','logentry'),(18,'auth','group'),(17,'auth','permission'),(19,'auth','user'),(13,'classe','classe'),(20,'contenttypes','contenttype'),(2,'district','district'),(12,'familia','familia'),(14,'filo','filo'),(10,'genero','genero'),(5,'geography','geography'),(7,'identifier','identifier'),(1,'location','location'),(11,'ordem','ordem'),(6,'person','person'),(3,'province','province'),(4,'region','region'),(15,'reino','reino'),(21,'sessions','session'),(9,'species','specie');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'person','0001_initial','2020-07-18 21:35:27.475521'),(2,'actor','0001_initial','2020-07-18 21:35:27.488982'),(3,'contenttypes','0001_initial','2020-07-18 21:35:27.601433'),(4,'auth','0001_initial','2020-07-18 21:35:27.866799'),(5,'admin','0001_initial','2020-07-18 21:35:29.394976'),(6,'admin','0002_logentry_remove_auto_add','2020-07-18 21:35:29.665916'),(7,'admin','0003_logentry_add_action_flag_choices','2020-07-18 21:35:29.680628'),(8,'contenttypes','0002_remove_content_type_name','2020-07-18 21:35:29.830329'),(9,'auth','0002_alter_permission_name_max_length','2020-07-18 21:35:29.852259'),(10,'auth','0003_alter_user_email_max_length','2020-07-18 21:35:29.875307'),(11,'auth','0004_alter_user_username_opts','2020-07-18 21:35:29.891761'),(12,'auth','0005_alter_user_last_login_null','2020-07-18 21:35:29.969801'),(13,'auth','0006_require_contenttypes_0002','2020-07-18 21:35:29.976502'),(14,'auth','0007_alter_validators_add_error_messages','2020-07-18 21:35:29.993599'),(15,'auth','0008_alter_user_username_max_length','2020-07-18 21:35:30.016182'),(16,'auth','0009_alter_user_last_name_max_length','2020-07-18 21:35:30.038198'),(17,'auth','0010_alter_group_name_max_length','2020-07-18 21:35:30.062323'),(18,'auth','0011_update_proxy_permissions','2020-07-18 21:35:30.076247'),(19,'classe','0001_initial','2020-07-18 21:35:30.084246'),(20,'district','0001_initial','2020-07-18 21:35:30.104261'),(21,'familia','0001_initial','2020-07-18 21:35:30.123935'),(22,'filo','0001_initial','2020-07-18 21:35:30.143727'),(23,'genero','0001_initial','2020-07-18 21:35:30.163957'),(24,'geography','0001_initial','2020-07-18 21:35:30.178476'),(25,'identifier','0001_initial','2020-07-18 21:35:30.193979'),(26,'location','0001_initial','2020-07-18 21:35:30.201337'),(27,'ordem','0001_initial','2020-07-18 21:35:30.210373'),(28,'province','0001_initial','2020-07-18 21:35:30.219311'),(29,'region','0001_initial','2020-07-18 21:35:30.226031'),(30,'reino','0001_initial','2020-07-18 21:35:30.233291'),(31,'sessions','0001_initial','2020-07-18 21:35:30.275000'),(32,'species','0001_initial','2020-07-18 21:35:30.316207'),(33,'actor','0002_auto_20200718_2208','2020-07-18 22:08:27.859591'),(34,'classe','0002_auto_20200718_2208','2020-07-18 22:08:27.870346'),(35,'district','0002_auto_20200718_2208','2020-07-18 22:08:27.875305'),(36,'familia','0002_auto_20200718_2208','2020-07-18 22:08:27.880937'),(37,'filo','0002_auto_20200718_2208','2020-07-18 22:08:27.893516'),(38,'genero','0002_auto_20200718_2208','2020-07-18 22:08:27.903178'),(39,'geography','0002_auto_20200718_2208','2020-07-18 22:08:27.911288'),(40,'identifier','0002_auto_20200718_2208','2020-07-18 22:08:27.917649'),(41,'location','0002_auto_20200718_2208','2020-07-18 22:08:27.923007'),(42,'ordem','0002_auto_20200718_2208','2020-07-18 22:08:27.929064'),(43,'person','0002_auto_20200718_2208','2020-07-18 22:08:27.935801'),(44,'province','0002_auto_20200718_2208','2020-07-18 22:08:27.940464'),(45,'region','0002_auto_20200718_2208','2020-07-18 22:08:27.953602'),(46,'reino','0002_auto_20200718_2208','2020-07-18 22:08:27.959718'),(47,'species','0002_auto_20200718_2208','2020-07-18 22:08:27.966851'),(48,'person','0003_auto_20200718_2219','2020-07-18 22:19:23.621903');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('zv2bsc9igqjv7ccgfh8cpqs6nfrew9kz','ODZiZTY0ZjU5MTFmODI2YmY4ZjBjZTUxZGU5M2MxZjRiYzg0YTBjYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5NWExOGY2OTJkYmNkZmNmYWFjNDI0NjRlMjRkODdhNjhmNGNjZDIxIn0=','2020-08-08 10:14:09.995314');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `familia`
--

DROP TABLE IF EXISTS `familia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `familia` (
  `idfamilia` int(11) NOT NULL AUTO_INCREMENT,
  `familia` varchar(200) DEFAULT NULL,
  `idordem` int(11) DEFAULT NULL,
  PRIMARY KEY (`idfamilia`),
  KEY `fk_familia_1_idx` (`idordem`),
  CONSTRAINT `fk_familia_1` FOREIGN KEY (`idordem`) REFERENCES `ordem` (`idordem`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `familia`
--

LOCK TABLES `familia` WRITE;
/*!40000 ALTER TABLE `familia` DISABLE KEYS */;
/*!40000 ALTER TABLE `familia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filo`
--

DROP TABLE IF EXISTS `filo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `filo` (
  `idfilo` int(11) NOT NULL AUTO_INCREMENT,
  `filo` varchar(200) DEFAULT NULL,
  `idreino` int(11) DEFAULT NULL,
  PRIMARY KEY (`idfilo`),
  KEY `fk_filo_1_idx` (`idreino`),
  CONSTRAINT `fk_filo_1` FOREIGN KEY (`idreino`) REFERENCES `reino` (`idreino`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filo`
--

LOCK TABLES `filo` WRITE;
/*!40000 ALTER TABLE `filo` DISABLE KEYS */;
/*!40000 ALTER TABLE `filo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genero`
--

DROP TABLE IF EXISTS `genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `genero` (
  `idgenero` int(11) NOT NULL AUTO_INCREMENT,
  `genero` varchar(200) DEFAULT NULL,
  `idfamilia` int(11) DEFAULT NULL,
  PRIMARY KEY (`idgenero`),
  KEY `fk_genero_1_idx` (`idfamilia`),
  CONSTRAINT `fk_genero_1` FOREIGN KEY (`idfamilia`) REFERENCES `familia` (`idfamilia`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genero`
--

LOCK TABLES `genero` WRITE;
/*!40000 ALTER TABLE `genero` DISABLE KEYS */;
/*!40000 ALTER TABLE `genero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `geography`
--

DROP TABLE IF EXISTS `geography`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `geography` (
  `idgeo` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(200) DEFAULT NULL,
  `location` multipoint DEFAULT NULL,
  `latitude` decimal(10,0) DEFAULT NULL,
  `longitude` decimal(10,0) DEFAULT NULL,
  `idespecie` int(11) DEFAULT NULL,
  PRIMARY KEY (`idgeo`),
  KEY `fk_geography_1_idx` (`idespecie`),
  CONSTRAINT `fk_geography_1` FOREIGN KEY (`idespecie`) REFERENCES `specie` (`idspecie`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `geography`
--

LOCK TABLES `geography` WRITE;
/*!40000 ALTER TABLE `geography` DISABLE KEYS */;
/*!40000 ALTER TABLE `geography` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordem`
--

DROP TABLE IF EXISTS `ordem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ordem` (
  `idordem` int(11) NOT NULL AUTO_INCREMENT,
  `ordem` varchar(200) DEFAULT NULL,
  `idclasse` int(11) DEFAULT NULL,
  PRIMARY KEY (`idordem`),
  KEY `fk_ordem_1_idx` (`idclasse`),
  CONSTRAINT `fk_ordem_1` FOREIGN KEY (`idclasse`) REFERENCES `classe` (`idclasse`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordem`
--

LOCK TABLES `ordem` WRITE;
/*!40000 ALTER TABLE `ordem` DISABLE KEYS */;
/*!40000 ALTER TABLE `ordem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pessoa`
--

DROP TABLE IF EXISTS `pessoa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pessoa` (
  `idpessoa` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `apelido` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idpessoa`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pessoa`
--

LOCK TABLES `pessoa` WRITE;
/*!40000 ALTER TABLE `pessoa` DISABLE KEYS */;
/*!40000 ALTER TABLE `pessoa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provincia`
--

DROP TABLE IF EXISTS `provincia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `provincia` (
  `idprovincia` int(11) NOT NULL AUTO_INCREMENT,
  `provincia` varchar(45) DEFAULT NULL,
  `idregiao` int(11) DEFAULT NULL,
  PRIMARY KEY (`idprovincia`),
  KEY `fk_provincia_1_idx` (`idregiao`),
  CONSTRAINT `fk_provincia_1` FOREIGN KEY (`idregiao`) REFERENCES `regiao` (`idregiao`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provincia`
--

LOCK TABLES `provincia` WRITE;
/*!40000 ALTER TABLE `provincia` DISABLE KEYS */;
/*!40000 ALTER TABLE `provincia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regiao`
--

DROP TABLE IF EXISTS `regiao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `regiao` (
  `idregiao` int(11) NOT NULL,
  `regiao` varchar(45) DEFAULT NULL,
  `pais` varchar(45) DEFAULT 'Mozambique',
  PRIMARY KEY (`idregiao`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regiao`
--

LOCK TABLES `regiao` WRITE;
/*!40000 ALTER TABLE `regiao` DISABLE KEYS */;
/*!40000 ALTER TABLE `regiao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reino`
--

DROP TABLE IF EXISTS `reino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reino` (
  `idreino` int(11) NOT NULL AUTO_INCREMENT,
  `reino` varchar(200) NOT NULL DEFAULT '',
  PRIMARY KEY (`idreino`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reino`
--

LOCK TABLES `reino` WRITE;
/*!40000 ALTER TABLE `reino` DISABLE KEYS */;
/*!40000 ALTER TABLE `reino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specie`
--

DROP TABLE IF EXISTS `specie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `specie` (
  `idspecie` int(11) NOT NULL AUTO_INCREMENT,
  `specie` varchar(200) DEFAULT NULL,
  `habitat` varchar(200) DEFAULT NULL,
  `detalhes` varchar(1000) DEFAULT NULL,
  `nomecomum` varchar(200) DEFAULT NULL,
  `idgenero` int(11) DEFAULT NULL,
  `datacriacao` datetime DEFAULT NULL,
  PRIMARY KEY (`idspecie`),
  KEY `fk_specie_1_idx` (`idgenero`),
  CONSTRAINT `fk_specie_1` FOREIGN KEY (`idgenero`) REFERENCES `genero` (`idgenero`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specie`
--

LOCK TABLES `specie` WRITE;
/*!40000 ALTER TABLE `specie` DISABLE KEYS */;
INSERT INTO `specie` VALUES (1,'FD','RE','GF','ER',NULL,'2020-07-24 18:47:11');
/*!40000 ALTER TABLE `specie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'parkArea'
--

--
-- Dumping routines for database 'parkArea'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-02 21:09:19
