-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 05-10-2020 a las 04:25:36
-- Versión del servidor: 5.7.26
-- Versión de PHP: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `publicaciones`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `books`
--

DROP TABLE IF EXISTS `books`;
CREATE TABLE IF NOT EXISTS `books` (
  `idBook` int(11) NOT NULL AUTO_INCREMENT,
  `titleBook` varchar(100) NOT NULL,
  `descriptionBook` text NOT NULL,
  `priceBook` int(100) NOT NULL,
  PRIMARY KEY (`idBook`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `books`
--

INSERT INTO `books` (`idBook`, `titleBook`, `descriptionBook`, `priceBook`) VALUES
(1, 'LUCES DE BOHEMIA Esperpento', 'E E Calpe Madrid 1996 Rustica 216 paginas 11 x 17 cms Edicion A Zamora Vicente ColecciÃ n Austral nÂº A 1 A ATENCION: El contra reembolso (SIEMPRE MENSAJERIA) incrementa los gastos en 7 euros. Nº de ref. del artículo: A137055', 5),
(2, 'PROGRAMACIÓN ORIENTADA A OBJETOS CON C++ (5ª ED.) ', 'La programación orientada a objetos (POO) es una de las técnicas más modernas de desarrollo que trata de disminuir el coste del software, aumentando la eficiencia y reduciendo el tiempo de espera para la puesta.', 38),
(3, 'COMPUTING SS BOOK ', 'Career Paths: Computing is a new educational resource for all professionals who want to improve their English communication regarding computing. Incorporating career-specific vocabulary and contexts, each unit offers step-by-step instruction that immerses students  ', 20);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
