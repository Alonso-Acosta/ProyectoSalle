-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-06-2021 a las 04:44:27
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `t_instrumento`
--

CREATE TABLE `t_instrumento` (
  `id_instrumento` varchar(15) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `tipo_instr` varchar(30) NOT NULL,
  `tipo_practica` varchar(25) NOT NULL,
  `estado_instr` varchar(15) NOT NULL,
  `cod_seguridad` varchar(30) NOT NULL,
  `fecha_registro` date NOT NULL,
  `fabricante` varchar(30) NOT NULL,
  `valor` float NOT NULL,
  `id_banco` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `t_instrumento`
--

INSERT INTO `t_instrumento` (`id_instrumento`, `nombre`, `tipo_instr`, `tipo_practica`, `estado_instr`, `cod_seguridad`, `fecha_registro`, `fabricante`, `valor`, `id_banco`) VALUES
('147', 'multimetro', 'medidor', 'perreo', 'Wueno', '00001', '2021-02-15', 'multitech', 250000, '0'),
('1478', 'Fusible', 'electricos', 'libre', 'perreo', '001365', '2021-06-01', 'multitech', 25000, '0'),
('654', 'Fluke', 'Medicion', 'libre', 'perreo', '7777777', '2021-05-17', 'multitech', 3000, '0'),
('963', 'Fluke ABC', 'Medicion', 'Clases', 'REGULAR', '14789', '2021-06-02', 'Multitech', 80000, '0');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `t_laboratorista`
--

CREATE TABLE `t_laboratorista` (
  `id_laboratorista` varchar(15) NOT NULL,
  `cedula` varchar(12) NOT NULL,
  `nombres` varchar(25) NOT NULL,
  `apellidos` varchar(30) NOT NULL,
  `tel_fijo` varchar(8) NOT NULL,
  `celular` varchar(12) NOT NULL,
  `ciudad` varchar(20) NOT NULL,
  `fecha_nac` date NOT NULL,
  `direccion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `t_laboratorista`
--

INSERT INTO `t_laboratorista` (`id_laboratorista`, `cedula`, `nombres`, `apellidos`, `tel_fijo`, `celular`, `ciudad`, `fecha_nac`, `direccion`) VALUES
('45161004', '126304', 'Miguel', 'Rojas', '917508', '321225461', 'Sincelejo', '2000-10-15', 'calle walabi 4 2 sydni');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `t_maquina`
--

CREATE TABLE `t_maquina` (
  `id_maquina` varchar(15) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `tipo_maq` varchar(30) NOT NULL,
  `tipo_practica` varchar(25) NOT NULL,
  `fecha_registro` date NOT NULL,
  `fabricante` varchar(30) NOT NULL,
  `valor` float NOT NULL,
  `estado_maq` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `t_maquina`
--

INSERT INTO `t_maquina` (`id_maquina`, `nombre`, `tipo_maq`, `tipo_practica`, `fecha_registro`, `fabricante`, `valor`, `estado_maq`) VALUES
('541', 'CNC', 'DISEÑO', 'LIBRE', '2021-05-17', 'FAIA', 3000000, 'perreo'),
('127', 'MOTOMAN', 'DISEÑO Y PROGRAMACION', 'LIBRE', '2021-05-17', 'SUSKI', 7000000, 'perreo'),
('96354', 'Frezadora', 'Mecanizado', 'OCUPADO', '2021-06-02', 'SUSKI', 9850000, 'PARA REPARACION');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `t_reparacion`
--

CREATE TABLE `t_reparacion` (
  `id_reparacion` int(11) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `fecha_retorno` date NOT NULL,
  `descripcion` varchar(60) NOT NULL,
  `id_laboratorista` varchar(15) NOT NULL,
  `id_maquina` varchar(15) NOT NULL,
  `id_instrumento` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `t_reparacion`
--

INSERT INTO `t_reparacion` (`id_reparacion`, `fecha_ingreso`, `fecha_retorno`, `descripcion`, `id_laboratorista`, `id_maquina`, `id_instrumento`) VALUES
(85963, '2021-05-21', '2021-06-02', 'Se Realizaron Reparicion y limpieza', '45161004', ' ', '963');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `t_usuarios`
--

CREATE TABLE `t_usuarios` (
  `user` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `cedula` varchar(12) NOT NULL,
  `tipousuario` varchar(20) NOT NULL,
  `cod_estud` varchar(10) NOT NULL,
  `id_laboratorista` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `t_usuarios`
--

INSERT INTO `t_usuarios` (`user`, `password`, `cedula`, `tipousuario`, `cod_estud`, `id_laboratorista`) VALUES
('Jarri', '123', '789654123', 'laboratorista', '0', '4518579');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
