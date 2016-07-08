CREATE DATABASE  IF NOT EXISTS `wallsdb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `wallsdb`;
-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: wallsdb
-- ------------------------------------------------------
-- Server version	5.5.41-log

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
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (26,'Sed laoreet bibendum est lacinia auctor. Pellentesque id leo lectus. Aliquam dictum viverra dignissim. Nam a tellus velit. Nulla tortor dui, auctor ac ante eget, tempor facilisis mauris. Pellentesque blandit ligula sed purus faucibus lobortis. Pellentesque non sapien at eros dapibus euismod. Donec fringilla purus eget eros imperdiet luctus non fermentum nunc. Vestibulum mi nunc, laoreet sed tincidunt a, venenatis vel massa. Quisque non erat vehicula, molestie ante at, porttitor justo.','2016-07-08 00:32:47','2016-07-08 00:32:47',25,2),(27,'<h3>Post a Message</h3>','2016-07-08 00:43:05','2016-07-08 00:43:05',25,2),(28,'dfasgwasadf','2016-07-08 00:46:21','2016-07-08 00:46:21',28,2),(29,'sdfwgdfsdf','2016-07-08 01:19:16','2016-07-08 01:19:16',28,1),(30,'ddddsdfsdfdsfdsf','2016-07-08 01:37:33','2016-07-08 01:37:33',26,1),(33,'Sed laoreet bibendum est lacinia auctor. Pellentesque id leo lectus. Aliquam dictum viverra dignissim. Nam a tellus velit. Nulla tortor dui, auctor ac ante eget, tempor facilisis mauris. Pellentesque blandit ligula sed purus faucibus lobortis. Pellentesque non sapien at eros dapibus euismod. Donec fringilla purus eget eros imperdiet luctus non fermentum nunc. Vestibulum mi nunc, laoreet sed tincidunt a, venenatis vel massa. Quisque non erat vehicula, molestie ante at, porttitor justo.','2016-07-08 02:11:29','2016-07-08 02:11:29',26,3),(34,'YEAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH','2016-07-08 02:12:41','2016-07-08 02:12:41',29,3);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (25,'Sed laoreet bibendum est lacinia auctor. Pellentesque id leo lectus. Aliquam dictum viverra dignissim. Nam a tellus velit. Nulla tortor dui, auctor ac ante eget, tempor facilisis mauris. Pellentesque blandit ligula sed purus faucibus lobortis. Pellentesque non sapien at eros dapibus euismod. Donec fringilla purus eget eros imperdiet luctus non fermentum nunc. Vestibulum mi nunc, laoreet sed tincidunt a, venenatis vel massa. Quisque non erat vehicula, molestie ante at, porttitor justo.','2016-07-08 00:32:41','2016-07-08 00:32:41',2),(26,'tor ac ante eget, tempor facilisis mauris. Pellentesque blandit ligula sed purus faucibus lobortis. Pellentesque non sapien at eros dapibus euismod. Donec fringilla purus eget eros imperdiet luctus non fe','2016-07-08 00:43:20','2016-07-08 00:43:20',2),(28,'Hello, My name is Tommy Oh. Nice to meet you all. Yolo.','2016-07-08 00:45:48','2016-07-08 00:45:48',2),(29,'Sed laoreet bibendum est lacinia auctor. Pellentesque id leo lectus. Aliquam dictum viverra dignissim. Nam a tellus velit. Nulla tortor dui, auctor ac ante eget, tempor facilisis mauris. Pellentesque blandit ligula sed purus faucibus lobortis. Pellentesque non sapien at eros dapibus euismod. Donec fringilla purus eget eros imperdiet luctus non fermentum nunc. Vestibulum mi nunc, laoreet sed tincidunt a, venenatis vel massa. Quisque non erat vehicula, molestie ante at, porttitor justo.','2016-07-08 01:43:30','2016-07-08 01:43:30',1),(30,'Sed laoreet bibendum est lacinia auctor. Pellentesque id leo lectus. Aliquam dictum viverra dignissim. Nam a tellus velit. Nulla tortor dui, auctor ac ante eget, tempor facilisis mauris. Pellentesque blandit ligula sed purus faucibus lobortis. Pellentesque non sapien at eros dapibus euismod. Donec fringilla purus eget eros imperdiet luctus non fermentum nunc. Vestibulum mi nunc, laoreet sed tincidunt a, venenatis vel massa. Quisque non erat vehicula, molestie ante at, porttitor justo.','2016-07-08 02:11:14','2016-07-08 02:11:14',3);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pw_hash` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Tommy','Oh','tommy@dojo.com','$2b$12$JsarV5tBABdls/1UHYGa4ubeD52stkgT6au9UhRCFZA2LyMGSCcjK','2016-07-07 18:10:34','2016-07-07 18:10:34'),(2,'Munchies','Burrito','surfnturf@gmail.com','$2b$12$7BvGItTjYWkyycUUROWjn.oAQvlqcbnZBHbIAvEFx6CzT6HQq/ujK','2016-07-07 20:11:51','2016-07-07 20:11:51'),(3,'Meow','Ninja','ninja@dojo.com','$2b$12$UY8.zLLdTgwlXbpGN828O.pSUYOOO77E5c9yId686Y5GzJoVN0UtW','2016-07-08 02:11:06','2016-07-08 02:11:06');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-08  2:23:56
