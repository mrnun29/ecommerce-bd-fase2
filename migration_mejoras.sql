-- Script de migración para mejoras finales
-- Sistema de Comercio Electrónico

USE `ecommerce_db`;

-- 1. Agregar campo 'activo' a la tabla USUARIO
ALTER TABLE `USUARIO` 
ADD COLUMN `activo` BOOLEAN NOT NULL DEFAULT TRUE AFTER `rol`;

-- 2. Agregar campo 'telefono' a la tabla PROVEEDOR
ALTER TABLE `PROVEEDOR`
ADD COLUMN `telefono` VARCHAR(15) NULL AFTER `empresa`;

-- Actualizar todos los usuarios existentes como activos
UPDATE `USUARIO` SET `activo` = TRUE WHERE `activo` IS NULL;

SELECT 'Migración completada exitosamente' as status;
