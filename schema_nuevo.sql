-- Sistema de Gestión de Inventario y Ventas
-- Roles: Administrador, Trabajador, Proveedor
-- MySQL Database Schema

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

USE `ecommerce_db`;

-- Eliminar tablas antiguas relacionadas con clientes y pedidos online
DROP TABLE IF EXISTS `EFECTIVO`;
DROP TABLE IF EXISTS `TRANSFERENCIA`;
DROP TABLE IF EXISTS `TARJETA`;
DROP TABLE IF EXISTS `PAGO`;
DROP TABLE IF EXISTS `DEVOLUCION`;
DROP TABLE IF EXISTS `ENVIO`;
DROP TABLE IF EXISTS `CARRITO`;
DROP TABLE IF EXISTS `PEDIDO`;
DROP TABLE IF EXISTS `CLIENTE`;

-- Tabla DIRECCION
CREATE TABLE IF NOT EXISTS `DIRECCION` (
  `id_direccion` INT NOT NULL AUTO_INCREMENT,
  `calle` VARCHAR(45) NOT NULL,
  `numero` INT NULL,
  `ciudad` VARCHAR(45) NOT NULL,
  `codigo_postal` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`id_direccion`)
) ENGINE = InnoDB;

-- Tabla USUARIO (Solo 3 roles: Administrador, Trabajador, Proveedor)
CREATE TABLE IF NOT EXISTS `USUARIO` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `correo` VARCHAR(60) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `rol` ENUM('Administrador', 'Trabajador', 'Proveedor') NOT NULL,
  `id_direccion` INT NOT NULL,
  `activo` BOOLEAN DEFAULT TRUE,
  PRIMARY KEY (`id_usuario`),
  UNIQUE INDEX `correo_UNIQUE` (`correo` ASC),
  INDEX `fk_USUARIO_DIRECCION` (`id_direccion` ASC),
  CONSTRAINT `fk_USUARIO_DIRECCION`
    FOREIGN KEY (`id_direccion`)
    REFERENCES `DIRECCION` (`id_direccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla TELEFONO
CREATE TABLE IF NOT EXISTS `TELEFONO` (
  `id_telefono` INT NOT NULL AUTO_INCREMENT,
  `telefono` VARCHAR(45) NOT NULL,
  `id_usuario` INT NOT NULL,
  PRIMARY KEY (`id_telefono`, `id_usuario`),
  INDEX `id_usuario_idx` (`id_usuario` ASC),
  CONSTRAINT `fk_TELEFONO_USUARIO`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `USUARIO` (`id_usuario`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla PROVEEDOR (ahora relacionada directamente con USUARIO)
CREATE TABLE IF NOT EXISTS `PROVEEDOR` (
  `id_proveedor` INT NOT NULL AUTO_INCREMENT,
  `contacto` VARCHAR(45) NOT NULL,
  `empresa` VARCHAR(45) NOT NULL,
  `id_direccion` INT NOT NULL,
  `id_usuario` INT NULL,
  PRIMARY KEY (`id_proveedor`),
  INDEX `fk_PROVEEDOR_DIRECCION_idx` (`id_direccion` ASC),
  INDEX `fk_PROVEEDOR_USUARIO_idx` (`id_usuario` ASC),
  CONSTRAINT `fk_PROVEEDOR_DIRECCION`
    FOREIGN KEY (`id_direccion`)
    REFERENCES `DIRECCION` (`id_direccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_PROVEEDOR_USUARIO`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `USUARIO` (`id_usuario`)
    ON DELETE SET NULL
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla PRODUCTO
CREATE TABLE IF NOT EXISTS `PRODUCTO` (
  `id_producto` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(40) NOT NULL,
  `imagen` VARCHAR(200) NULL,
  `stock` INT NOT NULL DEFAULT 0,
  `nivel_minimo` INT NOT NULL DEFAULT 10,
  `descripcion` VARCHAR(200) NULL,
  `precio` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id_producto`)
) ENGINE = InnoDB;

-- Tabla VENTA (reemplaza PEDIDO para ventas directas del trabajador)
CREATE TABLE IF NOT EXISTS `VENTA` (
  `id_venta` INT NOT NULL AUTO_INCREMENT,
  `total` DECIMAL(10,2) NOT NULL,
  `fecha` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `metodo_pago` ENUM('Efectivo', 'Tarjeta', 'Transferencia') NOT NULL,
  `id_trabajador` INT NOT NULL,
  `notas` TEXT NULL,
  PRIMARY KEY (`id_venta`),
  INDEX `fk_VENTA_TRABAJADOR_idx` (`id_trabajador` ASC),
  CONSTRAINT `fk_VENTA_TRABAJADOR`
    FOREIGN KEY (`id_trabajador`)
    REFERENCES `USUARIO` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla DETALLE_VENTA (reemplaza CARRITO para items de cada venta)
CREATE TABLE IF NOT EXISTS `DETALLE_VENTA` (
  `id_detalle` INT NOT NULL AUTO_INCREMENT,
  `id_venta` INT NOT NULL,
  `id_producto` INT NOT NULL,
  `cantidad` INT NOT NULL DEFAULT 1,
  `precio_unitario` DECIMAL(10,2) NOT NULL,
  `subtotal` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id_detalle`),
  INDEX `fk_DETALLE_VENTA_idx` (`id_venta` ASC),
  INDEX `fk_DETALLE_PRODUCTO_idx` (`id_producto` ASC),
  CONSTRAINT `fk_DETALLE_VENTA`
    FOREIGN KEY (`id_venta`)
    REFERENCES `VENTA` (`id_venta`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_DETALLE_PRODUCTO`
    FOREIGN KEY (`id_producto`)
    REFERENCES `PRODUCTO` (`id_producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla AVASTECE (relación Proveedor-Producto)
CREATE TABLE IF NOT EXISTS `AVASTECE` (
  `id_abastecimiento` INT NOT NULL AUTO_INCREMENT,
  `PRODUCTO_id_producto` INT NOT NULL,
  `PROVEEDOR_id_proveedor` INT NOT NULL,
  `fecha_abastecimiento` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`id_abastecimiento`),
  INDEX `fk_AVASTECE_PRODUCTO_idx` (`PRODUCTO_id_producto` ASC),
  INDEX `fk_AVASTECE_PROVEEDOR_idx` (`PROVEEDOR_id_proveedor` ASC),
  CONSTRAINT `fk_AVASTECE_PRODUCTO`
    FOREIGN KEY (`PRODUCTO_id_producto`)
    REFERENCES `PRODUCTO` (`id_producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_AVASTECE_PROVEEDOR`
    FOREIGN KEY (`PROVEEDOR_id_proveedor`)
    REFERENCES `PROVEEDOR` (`id_proveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
