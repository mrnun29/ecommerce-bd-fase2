-- Agregar campo teléfono a la tabla PROVEEDOR
USE `ecommerce_db`;

ALTER TABLE `PROVEEDOR` 
ADD COLUMN `telefono` VARCHAR(20) NOT NULL AFTER `empresa`;
