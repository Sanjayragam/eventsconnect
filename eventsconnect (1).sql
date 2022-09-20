-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 20, 2022 at 10:31 PM
-- Server version: 8.0.29
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eventsconnect`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `userid` int DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`userid`, `name`, `email`, `password`) VALUES
(NULL, 'ieeesbgeci', 'ieeesbgeci@gecidukki.ac.in', 'ieee'),
(NULL, 'iste', 'iste@gmail.com', 'iste');

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
CREATE TABLE IF NOT EXISTS `events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `club` varchar(100) NOT NULL,
  `name` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `day` int NOT NULL,
  `month` int NOT NULL,
  `year` int NOT NULL,
  `monthword` varchar(60) NOT NULL,
  `time` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `venue` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `speaker` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `color` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `endtime` varchar(50) NOT NULL,
  `req_status` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT 'No requests',
  PRIMARY KEY (`id`),
  UNIQUE KEY `date_time_unique` (`date`,`time`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`id`, `club`, `name`, `date`, `day`, `month`, `year`, `monthword`, `time`, `venue`, `speaker`, `color`, `status`, `endtime`, `req_status`) VALUES
(1, 'fossgeci', 'Webinar on foss', '2022-09-22', 22, 9, 2022, 'September', '02:53', 'seminar hall', 'sanjay', 'blue', 'pending', '04:52', 'Requested by iste'),
(2, 'iste', 'Technical paper writing', '2022-09-23', 23, 9, 2022, 'September', '02:55', 'seminar hall', 'sanjay', 'red', 'approved', '02:56', 'Requested by fossgeci'),
(4, 'ieeesbgeci', 'webinar on hi', '2022-09-28', 28, 9, 2022, 'September', '06:03', 'seminar hall', 'sanjay', 'red', 'rejected', '03:06', 'Requested by fossgeci');

-- --------------------------------------------------------

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
CREATE TABLE IF NOT EXISTS `requests` (
  `name` varchar(300) NOT NULL,
  `club` varchar(100) NOT NULL,
  `date` varchar(50) NOT NULL,
  `time` varchar(20) NOT NULL,
  `requestedby` varchar(100) NOT NULL,
  `status` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'Request cancellation'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `userid` int DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userid`, `name`, `email`, `password`) VALUES
(NULL, 'ieeesbgeci', 'ieeesbgeci@gecidukki.ac.in', 'ieee'),
(NULL, 'fossgeci', 'fossgeci@gmail.com', 'foss'),
(NULL, 'iste', 'iste@gmail.com', 'iste');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
