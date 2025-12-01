-- Agregar campo activo a la tabla USUARIO
USE `ecommerce_db`;

ALTER TABLE `USUARIO` 
ADD COLUMN `activo` BOOLEAN NOT NULL DEFAULT TRUE AFTER `rol`;
