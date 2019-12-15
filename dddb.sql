-- MySQL dump 10.13  Distrib 8.0.18, for macos10.14 (x86_64)
--
-- Host: localhost    Database: Dongdong
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
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
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
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
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
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
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add administrator',1,'add_administrator'),(2,'Can change administrator',1,'change_administrator'),(3,'Can delete administrator',1,'delete_administrator'),(4,'Can view administrator',1,'view_administrator'),(5,'Can add enterprise',2,'add_enterprise'),(6,'Can change enterprise',2,'change_enterprise'),(7,'Can delete enterprise',2,'delete_enterprise'),(8,'Can view enterprise',2,'view_enterprise'),(9,'Can add farmers',3,'add_farmers'),(10,'Can change farmers',3,'change_farmers'),(11,'Can delete farmers',3,'delete_farmers'),(12,'Can view farmers',3,'view_farmers'),(17,'Can add needs',5,'add_needs'),(18,'Can change needs',5,'change_needs'),(19,'Can delete needs',5,'delete_needs'),(20,'Can view needs',5,'view_needs'),(21,'Can add log entry',6,'add_logentry'),(22,'Can change log entry',6,'change_logentry'),(23,'Can delete log entry',6,'delete_logentry'),(24,'Can view log entry',6,'view_logentry'),(25,'Can add permission',7,'add_permission'),(26,'Can change permission',7,'change_permission'),(27,'Can delete permission',7,'delete_permission'),(28,'Can view permission',7,'view_permission'),(29,'Can add group',8,'add_group'),(30,'Can change group',8,'change_group'),(31,'Can delete group',8,'delete_group'),(32,'Can view group',8,'view_group'),(33,'Can add user',9,'add_user'),(34,'Can change user',9,'change_user'),(35,'Can delete user',9,'delete_user'),(36,'Can view user',9,'view_user'),(37,'Can add content type',10,'add_contenttype'),(38,'Can change content type',10,'change_contenttype'),(39,'Can delete content type',10,'delete_contenttype'),(40,'Can view content type',10,'view_contenttype'),(41,'Can add session',11,'add_session'),(42,'Can change session',11,'change_session'),(43,'Can delete session',11,'delete_session'),(44,'Can view session',11,'view_session'),(45,'Can add farmers member',12,'add_farmersmember'),(46,'Can change farmers member',12,'change_farmersmember'),(47,'Can delete farmers member',12,'delete_farmersmember'),(48,'Can view farmers member',12,'view_farmersmember'),(49,'Can add foreman',13,'add_foreman'),(50,'Can change foreman',13,'change_foreman'),(51,'Can delete foreman',13,'delete_foreman'),(52,'Can view foreman',13,'view_foreman'),(61,'Can add django job',16,'add_djangojob'),(62,'Can change django job',16,'change_djangojob'),(63,'Can delete django job',16,'delete_djangojob'),(64,'Can view django job',16,'view_djangojob'),(65,'Can add django job execution',17,'add_djangojobexecution'),(66,'Can change django job execution',17,'change_djangojobexecution'),(67,'Can delete django job execution',17,'delete_djangojobexecution'),(68,'Can view django job execution',17,'view_djangojobexecution'),(69,'Can add order',18,'add_order'),(70,'Can change order',18,'change_order'),(71,'Can delete order',18,'delete_order'),(72,'Can view order',18,'view_order');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
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
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_apscheduler_djangojob`
--

DROP TABLE IF EXISTS `django_apscheduler_djangojob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `django_apscheduler_djangojob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `next_run_time` datetime(6) DEFAULT NULL,
  `job_state` longblob NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `django_apscheduler_djangojob_next_run_time_2f022619` (`next_run_time`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_apscheduler_djangojob`
--

LOCK TABLES `django_apscheduler_djangojob` WRITE;
/*!40000 ALTER TABLE `django_apscheduler_djangojob` DISABLE KEYS */;
INSERT INTO `django_apscheduler_djangojob` VALUES (1,'task_time','2019-12-14 08:01:00.000000',_binary '��\0\0\0\0\0\0}�(�version�K�id��	task_time��func��needs.views:my_job��trigger��apscheduler.triggers.cron��CronTrigger���)��}�(hK�timezone��pytz��_p���(�\rAsia/Shanghai�M\�qK\0�LMT�t�R��\nstart_date�N�end_date�N�fields�]�(� apscheduler.triggers.cron.fields��	BaseField���)��}�(�name��year��\nis_default���expressions�]��%apscheduler.triggers.cron.expressions��\rAllExpression���)��}��step�Nsbaubh�\nMonthField���)��}�(h�month�h�h ]�h$)��}�h\'Nsbaubh�DayOfMonthField���)��}�(h�day�h�h ]�h$)��}�h\'Nsbaubh�	WeekField���)��}�(h�week�h�h ]�h$)��}�h\'Nsbaubh�DayOfWeekField���)��}�(h�day_of_week�h�h ]�h\"�WeekdayRangeExpression���)��}�(h\'N�first�K\0�last�Kubaubh\Z)��}�(h�hour�h�h ]�h\"�RangeExpression���)��}�(h\'NhJKhKKubaubh\Z)��}�(h�minute�h�h ]�hQ)��}�(h\'NhJKhKKubaubh\Z)��}�(h�second�h�h ]�hQ)��}�(h\'NhJK\0hKK\0ubaube�jitter�Nub�executor��default��args�)�kwargs�}�h�my_job��misfire_grace_time�K�coalesce���\rmax_instances�K�\rnext_run_time��datetime��datetime���C\n\�\0\0\0\0�h(hM�pK\0�CST�t�R���R�u.');
/*!40000 ALTER TABLE `django_apscheduler_djangojob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_apscheduler_djangojobexecution`
--

DROP TABLE IF EXISTS `django_apscheduler_djangojobexecution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `django_apscheduler_djangojobexecution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(50) NOT NULL,
  `run_time` datetime(6) NOT NULL,
  `duration` decimal(15,2) DEFAULT NULL,
  `started` decimal(15,2) DEFAULT NULL,
  `finished` decimal(15,2) DEFAULT NULL,
  `exception` varchar(1000) DEFAULT NULL,
  `traceback` longtext,
  `job_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_apscheduler_d_job_id_daf5090a_fk_django_ap` (`job_id`),
  KEY `django_apscheduler_djangojobexecution_run_time_16edd96b` (`run_time`),
  CONSTRAINT `django_apscheduler_d_job_id_daf5090a_fk_django_ap` FOREIGN KEY (`job_id`) REFERENCES `django_apscheduler_djangojob` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_apscheduler_djangojobexecution`
--

LOCK TABLES `django_apscheduler_djangojobexecution` WRITE;
/*!40000 ALTER TABLE `django_apscheduler_djangojobexecution` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_apscheduler_djangojobexecution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'admin','logentry'),(8,'auth','group'),(7,'auth','permission'),(9,'auth','user'),(10,'contenttypes','contenttype'),(16,'django_apscheduler','djangojob'),(17,'django_apscheduler','djangojobexecution'),(5,'needs','needs'),(18,'order','order'),(11,'sessions','session'),(1,'user','administrator'),(2,'user','enterprise'),(3,'user','farmers'),(12,'user','farmersmember'),(13,'user','foreman');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-11-18 13:31:20.730078'),(2,'auth','0001_initial','2019-11-18 13:31:20.801762'),(3,'admin','0001_initial','2019-11-18 13:31:20.925140'),(4,'admin','0002_logentry_remove_auto_add','2019-11-18 13:31:20.965754'),(5,'admin','0003_logentry_add_action_flag_choices','2019-11-18 13:31:20.974225'),(6,'contenttypes','0002_remove_content_type_name','2019-11-18 13:31:21.022639'),(7,'auth','0002_alter_permission_name_max_length','2019-11-18 13:31:21.040908'),(8,'auth','0003_alter_user_email_max_length','2019-11-18 13:31:21.058620'),(9,'auth','0004_alter_user_username_opts','2019-11-18 13:31:21.066205'),(10,'auth','0005_alter_user_last_login_null','2019-11-18 13:31:21.088139'),(11,'auth','0006_require_contenttypes_0002','2019-11-18 13:31:21.089947'),(12,'auth','0007_alter_validators_add_error_messages','2019-11-18 13:31:21.096884'),(13,'auth','0008_alter_user_username_max_length','2019-11-18 13:31:21.121357'),(14,'auth','0009_alter_user_last_name_max_length','2019-11-18 13:31:21.148613'),(15,'auth','0010_alter_group_name_max_length','2019-11-18 13:31:21.161793'),(16,'auth','0011_update_proxy_permissions','2019-11-18 13:31:21.168926'),(17,'user','0001_initial','2019-11-18 13:31:21.201573'),(18,'needs','0001_initial','2019-11-18 13:31:21.215982'),(20,'sessions','0001_initial','2019-11-18 13:31:21.244809'),(21,'user','0002_auto_20191118_2155','2019-11-18 13:55:28.780626'),(22,'needs','0002_remove_needs_matchresult','2019-11-19 03:17:21.207075'),(23,'user','0003_auto_20191119_1117','2019-11-19 03:17:21.276618'),(24,'needs','0003_needs_matchresult','2019-11-19 03:17:21.335747'),(26,'needs','0004_auto_20191119_1545','2019-11-19 07:45:24.771750'),(28,'user','0004_auto_20191119_1545','2019-11-19 07:45:24.994498'),(29,'user','0005_enterprise_icon','2019-11-21 07:29:09.634458'),(30,'needs','0005_auto_20191125_0954','2019-11-25 01:54:51.354437'),(31,'user','0006_enterprise_scope','2019-11-25 01:54:51.371716'),(33,'user','0007_auto_20191126_2013','2019-11-26 12:13:28.899452'),(34,'user','0008_auto_20191126_2047','2019-11-26 12:47:26.551126'),(35,'needs','0006_auto_20191127_1758','2019-11-27 11:05:06.815372'),(36,'needs','0007_auto_20191127_1830','2019-11-27 11:05:06.866200'),(37,'needs','0008_auto_20191127_1934','2019-11-27 11:34:30.705071'),(38,'user','0009_auto_20191127_1934','2019-11-27 11:34:30.730845'),(39,'user','0010_foreman_phonenumber','2019-11-29 06:39:56.709689'),(40,'needs','0009_auto_20191129_1440','2019-11-29 06:40:06.891326'),(41,'user','0011_auto_20191202_1131','2019-12-02 03:31:35.157420'),(42,'needs','0010_auto_20191202_1201','2019-12-02 04:01:53.666199'),(43,'user','0012_auto_20191202_1833','2019-12-02 10:33:18.096257'),(44,'needs','0011_auto_20191202_1850','2019-12-02 10:51:02.342894'),(45,'user','0013_auto_20191202_1900','2019-12-02 11:00:07.088127'),(48,'user','0014_auto_20191202_2002','2019-12-02 12:02:19.453209'),(51,'django_apscheduler','0001_initial','2019-12-02 13:34:27.152933'),(52,'django_apscheduler','0002_auto_20180412_0758','2019-12-02 13:34:27.195532'),(53,'user','0015_auto_20191205_1543','2019-12-05 07:44:02.626668'),(56,'user','0016_auto_20191209_1547','2019-12-09 07:47:41.276796'),(57,'order','0001_initial','2019-12-09 07:59:22.854362');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `needs_needs`
--

DROP TABLE IF EXISTS `needs_needs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `needs_needs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `needsDes` varchar(500) DEFAULT NULL,
  `needsFarmerType` varchar(2000) DEFAULT NULL,
  `needsNum` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `needsTime` date NOT NULL,
  `needsLocation` varchar(1000) DEFAULT NULL,
  `needsType` varchar(200) NOT NULL,
  `enterId_id` int(11) DEFAULT NULL,
  `remarks` varchar(2000) DEFAULT NULL,
  `needsBeginTime` date DEFAULT NULL,
  `needsEndTime` date DEFAULT NULL,
  `nowNum` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `needs_needs_enterId_id_ef3ce962_fk_user_enterprise_id` (`enterId_id`),
  CONSTRAINT `needs_needs_enterId_id_ef3ce962_fk_user_enterprise_id` FOREIGN KEY (`enterId_id`) REFERENCES `user_enterprise` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `needs_needs`
--

LOCK TABLES `needs_needs` WRITE;
/*!40000 ALTER TABLE `needs_needs` DISABLE KEYS */;
INSERT INTO `needs_needs` VALUES (4,'hhhhh244','木工',5,1000,'2019-11-27','bj','匹配失败',1,'wuoo','2019-11-26','2019-11-18',0),(5,'hhhhh224','木工',5,1000,'2019-11-27','bj','匹配完成待支付',2,'wuoo','2019-11-26','2019-11-18',9),(6,'hhh224','木工',5,1000,'2019-11-27','bj','匹配失败',1,'wuoo','2019-11-26','2019-11-18',0),(7,'hh999224','木工',5,1000,'2019-11-27','bj','匹配完成待支付',2,'wuoo','2019-11-26','2019-11-18',10),(11,'weqe','木工',13,12,'2019-12-02','adsadssda','匹配失败',1,NULL,'2019-12-02','2019-12-05',0),(12,'qwe','木工',123,213,'2019-12-02','adsdasdas','匹配失败',1,NULL,'2019-12-02','2019-12-05',0),(13,'da','木工',213,213,'2019-12-02','daadasdas','匹配失败',1,NULL,'2019-12-02','2019-12-04',12),(14,'sda','木工',123,213,'2019-12-02','d s d 搭讪sad','匹配失败',1,NULL,'2019-12-02','2019-12-05',0),(15,'dsa','木工',213,123,'2019-12-02','dasdasdas','匹配失败',1,NULL,'2019-12-02','2019-12-06',12),(16,'eqw','木工',123,213,'2019-12-02','dadasdsa','匹配失败',1,NULL,'2019-12-02','2019-12-04',0),(17,'dsa','木工',213,13,'2019-12-02','dadasdas','匹配失败',1,NULL,'2019-12-02','2019-12-05',0),(18,'das','木工',213,213,'2019-12-02','dadasdas','匹配失败',1,NULL,'2019-12-02','2019-12-05',0),(19,'12a','木工',123,21,'2019-12-02','dasdasdas','匹配失败',1,NULL,'2019-12-02','2019-12-04',0),(20,'da','木工',123,213,'2019-12-02','dasdasdas','匹配失败',1,NULL,'2019-12-02','2019-12-05',0),(21,'eqw','木工',213,21,'2019-12-02','dasdasda','匹配完成待支付',2,NULL,'2019-12-02','2019-12-05',16),(22,'dasd','木工',123,231,'2019-12-02','wadsddsdsadsa','匹配中',2,NULL,'2019-12-03','2019-12-12',0),(23,'dasd','木工',312,123,'2019-12-02','dasdsadsa','匹配中',2,NULL,'2019-12-03','2019-12-12',0),(24,'sadd','木工',132,123,'2019-12-02','asddasfafasfa','匹配中',2,NULL,'2019-12-03','2019-12-11',0),(25,'rqwer','木工',213,4,'2019-12-03','fsadffsdfgdfsgs','匹配中',2,NULL,'2019-12-05','2019-12-20',0),(26,'sfa','木工',123,12443,'2019-12-03','fsdafdsafgdg','匹配中',2,NULL,'2019-12-05','2019-12-20',8),(27,'fadsfg','木工',213414,214,'2019-12-03','dsfafggdfsgdfdsh','匹配中',2,NULL,'2019-12-05','2019-12-19',0),(28,'gdsagd','木工',123,42,'2019-12-03','sfdaffdggdfsgs','匹配中',2,NULL,'2019-12-05','2019-12-12',0),(29,'gdagsg','木工',21321,543,'2019-12-03','dfgsgdfsghfhsd','匹配中',2,NULL,'2019-12-05','2019-12-19',0);
/*!40000 ALTER TABLE `needs_needs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `needs_needs_matchResult`
--

DROP TABLE IF EXISTS `needs_needs_matchResult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `needs_needs_matchResult` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `needs_id` int(11) NOT NULL,
  `farmers_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `needs_needs_matchResult_needs_id_farmersgroup_id_28077838_uniq` (`needs_id`,`farmers_id`),
  KEY `needs_needs_matchResult_farmers_id_6b49e427_fk_user_farmers_id` (`farmers_id`),
  CONSTRAINT `needs_needs_matchResult_farmers_id_6b49e427_fk_user_farmers_id` FOREIGN KEY (`farmers_id`) REFERENCES `user_farmers` (`id`),
  CONSTRAINT `needs_needs_matchResult_needs_id_fdf946b5_fk_needs_needs_id` FOREIGN KEY (`needs_id`) REFERENCES `needs_needs` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `needs_needs_matchResult`
--

LOCK TABLES `needs_needs_matchResult` WRITE;
/*!40000 ALTER TABLE `needs_needs_matchResult` DISABLE KEYS */;
INSERT INTO `needs_needs_matchResult` VALUES (1,21,24),(2,21,26),(4,21,32),(3,21,33),(5,21,40),(6,21,44),(9,26,31),(7,26,39),(8,26,46);
/*!40000 ALTER TABLE `needs_needs_matchResult` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_order`
--

DROP TABLE IF EXISTS `order_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `order_order` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `id` varchar(1000) NOT NULL,
  `money` double NOT NULL,
  `moneyToFarmers` double NOT NULL,
  `moneyToApp` double NOT NULL,
  `beginTime` datetime(6) NOT NULL,
  `lastModified` datetime(6) NOT NULL,
  `status` varchar(200) NOT NULL,
  `needId_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  KEY `order_order_needId_id_12ba200f_fk_needs_needs_id` (`needId_id`),
  CONSTRAINT `order_order_needId_id_12ba200f_fk_needs_needs_id` FOREIGN KEY (`needId_id`) REFERENCES `needs_needs` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_order`
--

LOCK TABLES `order_order` WRITE;
/*!40000 ALTER TABLE `order_order` DISABLE KEYS */;
INSERT INTO `order_order` VALUES (1,'20191209215019282124',0.985915492957746,0.788732394366197,0.197183098591549,'2019-12-09 13:50:19.704156','2019-12-09 13:50:19.709819','交易中',21),(2,'20191209215019692126',0.197183098591549,0.157746478873239,0.0394366197183099,'2019-12-09 13:50:19.711579','2019-12-09 13:50:19.717887','交易中',21),(3,'20191209215019012132',0.394366197183099,0.315492957746479,0.0788732394366197,'2019-12-09 13:50:19.719858','2019-12-09 13:50:19.724881','交易中',21),(4,'20191209215019322133',0.591549295774648,0.473239436619718,0.11830985915493,'2019-12-09 13:50:19.727708','2019-12-09 13:50:19.736547','交易中',21),(5,'20191209215019812140',0.0985915492957747,0.0788732394366197,0.0197183098591549,'2019-12-09 13:50:19.738834','2019-12-09 13:50:19.746027','交易中',21),(6,'20191209215019812144',0.295774647887324,0.236619718309859,0.0591549295774648,'2019-12-09 13:50:19.748115','2019-12-09 13:50:19.754249','交易中',21);
/*!40000 ALTER TABLE `order_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_order_farmers`
--

DROP TABLE IF EXISTS `order_order_farmers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `order_order_farmers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `farmers_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_order_farmers_order_id_farmers_id_b3c86ad4_uniq` (`order_id`,`farmers_id`),
  KEY `order_order_farmers_farmers_id_31a1bdba_fk_user_farmers_id` (`farmers_id`),
  CONSTRAINT `order_order_farmers_farmers_id_31a1bdba_fk_user_farmers_id` FOREIGN KEY (`farmers_id`) REFERENCES `user_farmers` (`id`),
  CONSTRAINT `order_order_farmers_order_id_dd2656e8_fk_order_order_p_id` FOREIGN KEY (`order_id`) REFERENCES `order_order` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_order_farmers`
--

LOCK TABLES `order_order_farmers` WRITE;
/*!40000 ALTER TABLE `order_order_farmers` DISABLE KEYS */;
INSERT INTO `order_order_farmers` VALUES (1,1,24),(2,2,26),(3,3,32),(4,4,33),(5,5,40),(6,6,44);
/*!40000 ALTER TABLE `order_order_farmers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_administrator`
--

DROP TABLE IF EXISTS `user_administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `user_administrator` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_administrator`
--

LOCK TABLES `user_administrator` WRITE;
/*!40000 ALTER TABLE `user_administrator` DISABLE KEYS */;
INSERT INTO `user_administrator` VALUES (6,'简亓','1234'),(8,'程以清','1234'),(9,'敖三','1234');
/*!40000 ALTER TABLE `user_administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_enterprise`
--

DROP TABLE IF EXISTS `user_enterprise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `user_enterprise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `password` varchar(5000) NOT NULL,
  `enterName` varchar(500) DEFAULT NULL,
  `authState` varchar(200) NOT NULL,
  `authAdvice` varchar(2000) DEFAULT NULL,
  `enterDes` varchar(1000) DEFAULT NULL,
  `scope` varchar(1000) DEFAULT NULL,
  `businessItemInsurance` varchar(100) DEFAULT NULL,
  `businessLicense` varchar(100) DEFAULT NULL,
  `constructionPermit` varchar(100) DEFAULT NULL,
  `constructionQUAL` varchar(100) DEFAULT NULL,
  `landUseCert` varchar(100) DEFAULT NULL,
  `noTaxExpStatement` varchar(100) DEFAULT NULL,
  `noticeOfBid` varchar(100) DEFAULT NULL,
  `nowProject` varchar(1000) DEFAULT NULL,
  `planningPermit` varchar(100) DEFAULT NULL,
  `securityLicense` varchar(100) DEFAULT NULL,
  `socialSecurityCert` varchar(100) DEFAULT NULL,
  `startReport` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_enterprise`
--

LOCK TABLES `user_enterprise` WRITE;
/*!40000 ALTER TABLE `user_enterprise` DISABLE KEYS */;
INSERT INTO `user_enterprise` VALUES (1,'ljx','pbkdf2_sha256$150000$ky3d64duwL6P$2SPNayuHICsxDDf35jYAeLvsm36cRcHZ74b0vT7iD4g=','夹心全球贸易公司','',NULL,NULL,NULL,'enterAuth/夹心全球贸易公司/190924123232845_resume-samples-201906_ad8TeB3.pdf','enterAuth/夹心全球贸易公司/190918065207609_Course_ontro-2019_fall.pdf','enterAuth/夹心全球贸易公司/190918065207609_Course_ontro-2019_fall_N4z3HlV.pdf','enterAuth/夹心全球贸易公司/190924123232845_resume-samples-201906.pdf','enterAuth/夹心全球贸易公司/190918065207609_Course_ontro-2019_fall_oxSX4pp.pdf','enterAuth/夹心全球贸易公司/190918065426175_Unit_1_Career_Planning_P8vkI4A.pdf','enterAuth/夹心全球贸易公司/190918065207609_Course_ontro-2019_fall_XMqDHrW.pdf',NULL,'enterAuth/夹心全球贸易公司/190918065426175_Unit_1_Career_Planning_Ohvidpb.pdf','enterAuth/夹心全球贸易公司/190918065426175_Unit_1_Career_Planning.pdf','enterAuth/夹心全球贸易公司/190918065207609_Course_ontro-2019_fall_yDEu1hB.pdf','enterAuth/夹心全球贸易公司/190918065207609_Course_ontro-2019_fall_er9eQJN.pdf'),(2,'dcx','pbkdf2_sha256$150000$ydzvZJhb0QIA$BmFo6MFXjl2z8/iRRYR9hmlaTLimS+fAml7Mb+3Uy9s=','小略公司','未通过','照片不行','略略略','钢筋/板工','','enterAuth/小程中国分部/20191209214629_39.jpg','','enterAuth/小程中国分部/20191209214156_57.jpg','','','','你猜猜我是什么工程','','enterAuth/小程中国分部/中国特色社会主义理论与实践研究13班_数字媒体与设计艺术学院_2019110908_何其映.pdf','','');
/*!40000 ALTER TABLE `user_enterprise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_farmers`
--

DROP TABLE IF EXISTS `user_farmers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `user_farmers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(2000) NOT NULL,
  `ingNeed_id` int(11) DEFAULT NULL,
  `memberNumber` int(11) NOT NULL,
  `classNumber` int(11) NOT NULL,
  `leader_id` int(11) DEFAULT NULL,
  `authState` varchar(2000) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_farmers_ingNeed_id_ae942f9e_fk_needs_needs_id` (`ingNeed_id`),
  KEY `user_farmers_leader_id_7998557c_fk_user_foreman_id` (`leader_id`),
  CONSTRAINT `user_farmers_ingNeed_id_ae942f9e_fk_needs_needs_id` FOREIGN KEY (`ingNeed_id`) REFERENCES `needs_needs` (`id`),
  CONSTRAINT `user_farmers_leader_id_7998557c_fk_user_foreman_id` FOREIGN KEY (`leader_id`) REFERENCES `user_foreman` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_farmers`
--

LOCK TABLES `user_farmers` WRITE;
/*!40000 ALTER TABLE `user_farmers` DISABLE KEYS */;
INSERT INTO `user_farmers` VALUES (8,'木工',NULL,0,1,5,'审核未通过'),(9,'木工',NULL,0,2,5,'审核未通过'),(10,'木工',22,0,3,5,'审核通过'),(11,'木工',NULL,0,4,5,'审核未通过'),(12,'泥瓦工',NULL,0,1,5,'审核通过'),(13,'泥瓦工',NULL,1,2,5,'审核中'),(14,'电工',23,0,1,5,'审核通过'),(15,'木工',NULL,0,5,4,'审核未通过'),(16,'木工',NULL,0,6,4,'审核未通过'),(17,'电工',NULL,0,2,4,'审核未通过'),(18,'木工',NULL,0,7,4,'审核通过'),(19,'混凝土',NULL,0,1,4,'审核未通过'),(20,'混凝土',NULL,0,2,4,'审核未通过'),(21,'架子工',NULL,1,1,6,'审核中'),(22,'防水',NULL,0,1,6,'审核通过'),(23,'木工',NULL,1,8,6,'审核中'),(24,'木工',21,10,9,10,'审核中'),(25,'其他',NULL,3,1,10,'审核中'),(26,'木工',21,2,10,10,'审核中'),(27,'钢筋班组',NULL,0,1,10,'审核中'),(28,'混凝土',NULL,1,3,6,'审核中'),(29,'混凝土',NULL,0,4,10,'审核通过'),(30,'油漆',NULL,1,1,10,'审核中'),(31,'木工',26,3,11,10,'审核通过'),(32,'木工',21,4,12,10,'审核通过'),(33,'木工',21,6,13,10,'审核通过'),(34,'架子工',NULL,3,2,9,'审核中'),(35,'砌砖',NULL,0,1,11,'审核通过'),(36,'混凝土',NULL,0,5,9,'审核中'),(37,'油漆',NULL,1,2,9,'审核通过'),(38,'木工',NULL,0,14,12,'审核通过'),(39,'木工',26,1,15,11,'审核通过'),(40,'木工',21,1,16,13,'审核通过'),(41,'木工',NULL,2,17,9,'审核中'),(42,'木工',NULL,4,18,10,'审核通过'),(43,'木工',NULL,3,19,10,'审核中'),(44,'木工',21,3,20,10,'审核通过'),(45,'木工',NULL,3,21,10,'审核中'),(46,'木工',26,4,22,10,'审核通过'),(47,'木工',NULL,3,23,10,'审核通过'),(48,'木工',NULL,0,24,6,'审核中'),(49,'木工',NULL,0,25,6,'审核中'),(50,'木工',NULL,0,26,6,'审核中'),(51,'钢筋班组',NULL,0,2,6,'审核中'),(52,'架子工',NULL,0,3,6,'审核中'),(53,'混凝土',NULL,0,6,6,'审核中'),(54,'木工',NULL,0,27,10,'审核中'),(55,'木工',NULL,1,28,11,'审核中');
/*!40000 ALTER TABLE `user_farmers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_farmersmember`
--

DROP TABLE IF EXISTS `user_farmersmember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `user_farmersmember` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `IDCard` varchar(100) NOT NULL,
  `authInfo` varchar(100) DEFAULT NULL,
  `phoneNumber` varchar(100) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_farmersmember_group_id_7157fac9_fk_user_farmers_id` (`group_id`),
  CONSTRAINT `user_farmersmember_group_id_7157fac9_fk_user_farmers_id` FOREIGN KEY (`group_id`) REFERENCES `user_farmers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_farmersmember`
--

LOCK TABLES `user_farmersmember` WRITE;
/*!40000 ALTER TABLE `user_farmersmember` DISABLE KEYS */;
INSERT INTO `user_farmersmember` VALUES (11,'tnt1','12343536','','1234255',10),(12,'tnt2','12343536','','1234255',10),(13,'tnt3','12343536','','1234255',10),(14,'发','','','1313',24),(15,'李桐','130730199595130612','','13171639286',24),(16,'往','13011111111','','1231',24),(17,'韩玉鑫','111111111111111111','','11111111111',25),(18,'小丁','1232','','12343',13),(19,'李桐','222222222222222222','','33333333333',25),(20,'魏欣莉','333333333333333333','','33333333333',25),(21,'高万振','1316431649763319','','1346779916766',23),(22,'何日子','11111111','','',21),(23,'李桐','11111111111111','','11111111',30),(24,'M1','1','','1',26),(25,'M2','2','','2',26),(26,'M1','1','','1',31),(27,'M2','2','','2',31),(28,'M3','3','','3',31),(29,'A1','1','','1',32),(30,'A2','2','','2',32),(31,'A3','3','','3',32),(32,'A4','4','','4',32),(33,'B1','1','','1',33),(34,'B2','2','','2',33),(35,'B3','3','','3',33),(36,'B4','4','','4',33),(37,'B5','5','','5',33),(38,'B6','6','','6',33),(39,'hhhh','111111','','13788888888',34),(40,'aaaaa','88888','','99999',34),(41,'铁柱','12000000000000007','','13677777666',34),(42,'嘻嘻嘻','189098888888888888','','16792635241',37),(43,'高大帅','123','','456',39),(44,'久哦哦','125896332586692','','175256399853',40),(45,'铁柱柱','12000000000','','12777777777',41),(46,'小小军','87877799898','','12766666541',41),(47,'M1','1','','1',42),(48,'2','23','','23',42),(49,'2132','123','','123',42),(50,'123213','123','','123213',42),(51,'123123','2131232','','123232',47),(52,'23123','1233333','','23123',47),(53,'123DASD','ASDASD','','ASDASD',47),(54,'ASDA','SADA','','ADAFBVBN',46),(55,'VNG','GNERG','','BBGNTH',46),(56,'DFGG','DRGDR','','DFDFG',46),(57,'FGDGD','DFGDD','','WERW3R',46),(58,'ASDAWE','GDGGN','','DCDVV',45),(59,'WAD23','2ASDV','','BNYK7THH',45),(60,'WDAASDN V','BB','','BV',45),(61,'ASDASD','ASCXVL','','LK.K.',43),(62,'JK.','.JK.','','M',43),(63,'KGJ','JHK','','HJKHK',43),(64,'HJKHJ','MN,FGH','','NM,NMJGJGHV',44),(65,'SDA','ASD','','ACZX',44),(66,'ZXCZ','ZXCADAQ','','ASD',44),(67,'阿','阿','','阿',24),(68,'嗄','a','http://tmp/wx2e0f6900788aba6c.o6zAJs28YwoZFqfRAp4K2FIAky7g.ZJqgpgE0o3Q166c350619d4f00e29ed92f3a50343','1',24),(69,'a111','暗示','http://tmp/wx2e0f6900788aba6c.o6zAJs28YwoZFqfRAp4K2FIAky7g.HLbkg8Fkj6yl66c3b50619d4f00e29ed92f3a5034','333',24),(70,'嗷嗷','342343','','123243',24),(71,'嗷嗷','342343','farmerAuth/QQ20190828-0.jpg','123243',24),(72,'11','22333','farmerAuth/wx2e0f6900788aba6c.o6zAJs28YwoZFqfRAp4K2FIAky7g.nnHV2dW4XfdL66c3b50619d4f00e2_rwf9BSH.jpg','3',24),(73,'xxx','4536474','farmerAuth/QQ20190828-2.jpg','132453',28),(74,'1','1','farmerAuth/wx2e0f6900788aba6c.o6zAJs28YwoZFqfRAp4K2FIAky7g.xaW9p3GtAoG566c3b50619d4f00e2_2CEdSPC.jpg','1',24),(75,'1','1','farmerAuth/wx2e0f6900788aba6c.o6zAJs28YwoZFqfRAp4K2FIAky7g.xaW9p3GtAoG566c3b50619d4f00e2_SRK6EBc.jpg','1',24),(76,'1','1','farmerAuth/wx2e0f6900788aba6c.o6zAJs28YwoZFqfRAp4K2FIAky7g.poBzD6CKgbDy66c3b50619d4f00e2_2TNIC6p.jpg','1',24),(77,'1','1','farmerAuth/wx2e0f6900788aba6c.o6zAJs28YwoZFqfRAp4K2FIAky7g.wHUasIpqCJRdb831469c2703cedb3_xjE9920.jpg','1',24),(78,'123','222','farmerAuth/tmp_9cb51cd0627618739f2d034ffa8f7b86b13de48481d47288.jpg','222',55);
/*!40000 ALTER TABLE `user_farmersmember` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_foreman`
--

DROP TABLE IF EXISTS `user_foreman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `user_foreman` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `password` varchar(5000) NOT NULL,
  `openid` varchar(5000) NOT NULL,
  `IDCard` varchar(100) DEFAULT NULL,
  `phonenumber` varchar(100) DEFAULT NULL,
  `Bank` varchar(100) DEFAULT NULL,
  `BankNumber` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_foreman`
--

LOCK TABLES `user_foreman` WRITE;
/*!40000 ALTER TABLE `user_foreman` DISABLE KEYS */;
INSERT INTO `user_foreman` VALUES (4,'','pbkdf2_sha256$150000$a6po1GqQYjHA$bDCYlERmO6Q86763InW/8Q7vU/LOvT4JM2pXwangw9s=','oVenj5Lmh6aO6MejsQatoI3xT8pk','','',NULL,NULL),(5,'丁程鑫','pbkdf2_sha256$150000$rJ9XGSnSwV9K$aITYhE2U00HAE3/SmzSTCmGEbi2uAgK+r+da+vz+N9w=','oVenj5Lmh6aO6MejsQatoI3xT8pk','123456','1323453','中国建设银行','62229999999'),(6,'李桐','pbkdf2_sha256$150000$Aa6AOEWhSCJg$mQPlWwquReoG4vpb6KyOjm3g1kgATqsnkOzHa2NrSdo=','oVenj5Lmh6aO6MejsQatoI3xT8pk','1313134661946','1679949195','中国银行卡好','16769485946'),(8,'产品魏','pbkdf2_sha256$150000$LFfFLReIyDym$z9X6OgC2dHLv5RTqLCX+5Mut8SYPMUfmxGJ+YkAlC9w=','oVenj5LKOxdAJ6SD7nvWKXdK1TfY',NULL,NULL,NULL,NULL),(9,'gao','pbkdf2_sha256$150000$z2ZobGQ1CFPm$Uur+83UdfKV17ZTFGqn/iNVsX9SNXdgRBxmtSj2fF1w=','oVenj5NOtmMiXwiRPbsS6seCG72s','88888888','666666','中国银行','8886666'),(10,'韩玉鑫','pbkdf2_sha256$150000$ApDOgpd79vqv$IwuFmgP4hWND1qCxZDdvrFmebOjCyBpe6STUP4c7N8Q=','oVenj5Lmh6aO6MejsQatoI3xT8pk','111111111111111111','11111111111','中国农业银行','1111111111111111111111111'),(11,'Shirley wei','pbkdf2_sha256$150000$ovRNh7TqtrB0$Kukr14HO1qGmzhp17bsxLKrwSLAzZaOH0Efkj49fR4w=','oVenj5LKOxdAJ6SD7nvWKXdK1TfY','1111','2222','3333','4444'),(12,'大哥','pbkdf2_sha256$150000$5u1kwjJ9pR1D$8x4wyw6EUUwMNiyRBaWXKeqauKhDQk8TNuM6q0YUodQ=','oVenj5NDvXDtyg-Kxou4MxCTSsnw',NULL,NULL,NULL,NULL),(13,'李桐桐','pbkdf2_sha256$150000$zNqdJwNhYpJB$sG5PbByHvoM7EVRsfe90jOIubLNTZRxcQNEN3X5+8kQ=','oVenj5M1BokWuK331Jc5KnCmfSkY','111111111111111111','11111111111','李桐银行有限公司','11111111111');
/*!40000 ALTER TABLE `user_foreman` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-14  0:42:34
