-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: yourSpot
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `user_saved_restaurants`
--

DROP TABLE IF EXISTS `user_saved_restaurants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_saved_restaurants` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `restaurant_id` int NOT NULL,
  `user_rating` int DEFAULT NULL,
  `review` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date_reviewed` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `User_Saved_Restaurants_FK` (`restaurant_id`),
  KEY `User_Saved_Restaurants_FK_1` (`user_id`),
  CONSTRAINT `User_Saved_Restaurants_FK` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`id`),
  CONSTRAINT `User_Saved_Restaurants_FK_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_saved_restaurants`
--

LOCK TABLES `user_saved_restaurants` WRITE;
/*!40000 ALTER TABLE `user_saved_restaurants` DISABLE KEYS */;
INSERT INTO `user_saved_restaurants` VALUES (2,2,2,5,'beef beef beef','2018-05-09'),(3,3,3,4,'Lighting is too dim','2010-10-19'),(5,5,5,3,'Best Pad Thai','2016-10-21'),(9,1,1,1,'they put spice when i asked for mild :(','2020-11-23'),(10,4,1,5,'Best Jerk no cap','2020-11-23'),(11,1,1,4,'its good','2020-11-23'),(12,4,3,5,'BEST PASTA OMGGG','2020-11-24'),(14,11,5,5,'Best Pad Thai','2020-11-25'),(15,11,1,4,'Pretty Decent','2020-11-25'),(18,4,1,5,'good','2020-11-25');
/*!40000 ALTER TABLE `user_saved_restaurants` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-26 11:33:53
