-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: project0
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
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dish_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `flavour_profile` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT ' comma separated values',
  `price` float DEFAULT NULL,
  `rating` int DEFAULT NULL,
  `restaurant_id` int NOT NULL,
  `allergies` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'comma separated values',
  PRIMARY KEY (`id`),
  KEY `Menu_FK` (`restaurant_id`),
  CONSTRAINT `Menu_FK` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Jerk Chicken','Jerk seasoned chicken w/ rice & peas or fries','spicy',11.99,4,1,NULL),(2,'club sandwhich','Triple decker sandwhich w/ chicken, lettuce, tomato, cheese, mayo, and bacon','sandwhich',10.5,3,4,NULL),(3,'Fettuccini alfredo','Creamy alfreado sauce with peccorino and fettuccini noodles.','Italian, pasta',19,5,3,'gluten'),(4,'T-bone steak','8oz top sirloin seared to perfection!','Red meat, american',37,5,2,NULL),(5,'Pad thai','Noodles, protien of choice, veggies, pad thai sauce. Choose your heat level','Thai, asian, spicy',20,4,5,'nut'),(6,'Ceasar salad','Romaine Lettuce, homemade crutons, bacon & parm','salad',14,3,6,NULL),(7,'Ox Tail & Rice','Ox tail, seasoned rice, & salad','carribean, meat',12.99,4,1,NULL),(8,'Chicken Parm','Fried chicken, with housemade tomato sauce and parm','italian, fried',14.99,4,3,NULL),(9,'Fish n\' Chips','Cod and fries with tartar sauce on the side','fried, bar',10.99,3,4,NULL),(10,'Mac n Cheese','Classic maccaroni and cheese','pasta',12,3,6,NULL),(11,'Som Tum','green papaya, thai chilly, peanut, and sweet sauce','salad, spicy',11.95,5,5,'nut'),(12,'Filet Mignon','10oz, wrapped with bacon','red meat, american',42,5,2,NULL);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
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
