-- Sistema de Comercio Electrónico con Gestión de Inventarios
-- Bases de Datos - Fase 2
-- MySQL Database Schema

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- Usar base de datos (ya creada por Docker)
USE `ecommerce_db`;

-- Tabla DIRECCION
CREATE TABLE IF NOT EXISTS `DIRECCION` (
  `id_direccion` INT NOT NULL AUTO_INCREMENT,
  `calle` VARCHAR(45) NOT NULL,
  `numero` INT NULL,
  `ciudad` VARCHAR(45) NOT NULL,
  `codigo_postal` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`id_direccion`)
) ENGINE = InnoDB;

-- Tabla USUARIO
CREATE TABLE IF NOT EXISTS `USUARIO` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `correo` VARCHAR(60) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `rol` ENUM('Administrador', 'Empleado', 'Cliente') NOT NULL DEFAULT 'Cliente',
  `id_direccion` INT NOT NULL,
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

-- Tabla CLIENTE
CREATE TABLE IF NOT EXISTS `CLIENTE` (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `historial_compras` TEXT NULL,
  `id_usuario` INT NOT NULL,
  PRIMARY KEY (`id_cliente`),
  INDEX `fk_CLIENTE_USUARIO_idx` (`id_usuario` ASC),
  CONSTRAINT `fk_CLIENTE_USUARIO`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `USUARIO` (`id_usuario`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla PROVEEDOR
CREATE TABLE IF NOT EXISTS `PROVEEDOR` (
  `id_proveedor` INT NOT NULL AUTO_INCREMENT,
  `contacto` VARCHAR(45) NOT NULL,
  `empresa` VARCHAR(45) NOT NULL,
  `id_direccion` INT NOT NULL,
  PRIMARY KEY (`id_proveedor`),
  INDEX `fk_PROVEEDOR_DIRECCION_idx` (`id_direccion` ASC),
  CONSTRAINT `fk_PROVEEDOR_DIRECCION`
    FOREIGN KEY (`id_direccion`)
    REFERENCES `DIRECCION` (`id_direccion`)
    ON DELETE NO ACTION
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

-- Tabla PEDIDO
CREATE TABLE IF NOT EXISTS `PEDIDO` (
  `id_pedido` INT NOT NULL AUTO_INCREMENT,
  `total` DECIMAL(10,2) NOT NULL,
  `fecha` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `estado` ENUM('Pendiente', 'Procesando', 'Enviado', 'Entregado', 'Cancelado') NOT NULL DEFAULT 'Pendiente',
  `id_cliente` INT NOT NULL,
  PRIMARY KEY (`id_pedido`),
  INDEX `fk_PEDIDO_CLIENTE_idx` (`id_cliente` ASC),
  CONSTRAINT `fk_PEDIDO_CLIENTE`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `CLIENTE` (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla CARRITO
CREATE TABLE IF NOT EXISTS `CARRITO` (
  `PRODUCTO_id_producto` INT NOT NULL,
  `PEDIDO_id_pedido` INT NOT NULL,
  `cantidad` INT NOT NULL DEFAULT 1,
  `precio_unitario` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`PRODUCTO_id_producto`, `PEDIDO_id_pedido`),
  INDEX `fk_CARRITO_PEDIDO_idx` (`PEDIDO_id_pedido` ASC),
  CONSTRAINT `fk_CARRITO_PRODUCTO`
    FOREIGN KEY (`PRODUCTO_id_producto`)
    REFERENCES `PRODUCTO` (`id_producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CARRITO_PEDIDO`
    FOREIGN KEY (`PEDIDO_id_pedido`)
    REFERENCES `PEDIDO` (`id_pedido`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla PAGO
CREATE TABLE IF NOT EXISTS `PAGO` (
  `id_pago` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `monto` DECIMAL(10,2) NOT NULL,
  `tipo_pago` ENUM('Tarjeta', 'Transferencia', 'Efectivo') NOT NULL,
  `id_pedido` INT NOT NULL,
  PRIMARY KEY (`id_pago`),
  INDEX `fk_PAGO_PEDIDO_idx` (`id_pedido` ASC),
  CONSTRAINT `fk_PAGO_PEDIDO`
    FOREIGN KEY (`id_pedido`)
    REFERENCES `PEDIDO` (`id_pedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla TARJETA
CREATE TABLE IF NOT EXISTS `TARJETA` (
  `id_tarjeta` INT NOT NULL AUTO_INCREMENT,
  `num_tarjeta` VARCHAR(45) NOT NULL,
  `banco` VARCHAR(20) NOT NULL,
  `vencimiento` DATE NOT NULL,
  `cuenta` VARCHAR(20) NOT NULL,
  `id_pago` INT NOT NULL,
  PRIMARY KEY (`id_tarjeta`),
  INDEX `fk_TARJETA_PAGO_idx` (`id_pago` ASC),
  CONSTRAINT `fk_TARJETA_PAGO`
    FOREIGN KEY (`id_pago`)
    REFERENCES `PAGO` (`id_pago`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla TRANSFERENCIA
CREATE TABLE IF NOT EXISTS `TRANSFERENCIA` (
  `id_transferencia` INT NOT NULL AUTO_INCREMENT,
  `referencia` VARCHAR(25) NOT NULL,
  `id_pago` INT NOT NULL,
  PRIMARY KEY (`id_transferencia`),
  INDEX `fk_TRANSFERENCIA_PAGO_idx` (`id_pago` ASC),
  CONSTRAINT `fk_TRANSFERENCIA_PAGO`
    FOREIGN KEY (`id_pago`)
    REFERENCES `PAGO` (`id_pago`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla EFECTIVO
CREATE TABLE IF NOT EXISTS `EFECTIVO` (
  `id_efectivo` INT NOT NULL AUTO_INCREMENT,
  `folio` INT NOT NULL,
  `fecha_limite` DATE NOT NULL,
  `id_pago` INT NOT NULL,
  PRIMARY KEY (`id_efectivo`),
  INDEX `fk_EFECTIVO_PAGO_idx` (`id_pago` ASC),
  CONSTRAINT `fk_EFECTIVO_PAGO`
    FOREIGN KEY (`id_pago`)
    REFERENCES `PAGO` (`id_pago`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla ENVIO
CREATE TABLE IF NOT EXISTS `ENVIO` (
  `id_envio` INT NOT NULL AUTO_INCREMENT,
  `estado_envio` ENUM('Camino', 'En entrega', 'Recibido') NOT NULL DEFAULT 'Camino',
  `fecha_envio` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `direccion` VARCHAR(45) NOT NULL,
  `tipo` ENUM('Express', 'Gratis', 'Internacional') NOT NULL,
  `costo_extra` DECIMAL(10,2) NOT NULL DEFAULT 0,
  `id_pedido` INT NOT NULL,
  PRIMARY KEY (`id_envio`),
  INDEX `fk_ENVIO_PEDIDO_idx` (`id_pedido` ASC),
  CONSTRAINT `fk_ENVIO_PEDIDO`
    FOREIGN KEY (`id_pedido`)
    REFERENCES `PEDIDO` (`id_pedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla DEVOLUCION
CREATE TABLE IF NOT EXISTS `DEVOLUCION` (
  `id_devolucion` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `motivo` VARCHAR(45) NULL,
  `estado` ENUM('Nuevo', 'Casi Nuevo', 'Usado', 'Roto') NOT NULL,
  `id_pedido` INT NOT NULL,
  PRIMARY KEY (`id_devolucion`),
  INDEX `fk_DEVOLUCION_PEDIDO_idx` (`id_pedido` ASC),
  CONSTRAINT `fk_DEVOLUCION_PEDIDO`
    FOREIGN KEY (`id_pedido`)
    REFERENCES `PEDIDO` (`id_pedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla AVASTECE
CREATE TABLE IF NOT EXISTS `AVASTECE` (
  `PRODUCTO_id_producto` INT NOT NULL,
  `PROVEEDOR_id_proveedor` INT NOT NULL,
  `fecha_abastecimiento` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`PRODUCTO_id_producto`, `PROVEEDOR_id_proveedor`),
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
