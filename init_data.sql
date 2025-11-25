-- Datos de prueba para el sistema de E-Commerce
USE ecommerce_db;

-- Insertar direcciones
INSERT INTO DIRECCION (calle, numero, ciudad, codigo_postal) VALUES
('Av. Principal', 100, 'Querétaro', '76000'),
('Calle Trabajo', 50, 'Querétaro', '76010'),
('Calle Residencial', 25, 'Querétaro', '76020'),
('Zona Industrial', 500, 'Querétaro', '76120'),
('Parque Industrial', 300, 'Querétaro', '76130');

-- Insertar usuarios (contraseñas hasheadas con scrypt - admin123, empleado123, cliente123)
INSERT INTO USUARIO (nombre, correo, password, rol, id_direccion) VALUES
('Admin Principal', 'admin@ecommerce.com', 'scrypt:32768:8:1$salt123$hashedpassword', 'Administrador', 1),
('Juan Empleado', 'empleado@ecommerce.com', 'scrypt:32768:8:1$salt456$hashedpassword', 'Empleado', 2),
('María Cliente', 'cliente@email.com', 'scrypt:32768:8:1$salt789$hashedpassword', 'Cliente', 3);

-- Insertar cliente
INSERT INTO CLIENTE (id_usuario, historial_compras) VALUES
(3, '');

-- Insertar proveedores
INSERT INTO PROVEEDOR (contacto, empresa, id_direccion) VALUES
('Carlos López', 'Distribuidora Tech SA', 4),
('Ana García', 'Importaciones Global', 5);

-- Insertar productos
INSERT INTO PRODUCTO (nombre, descripcion, precio, stock, nivel_minimo, imagen) VALUES
('Laptop HP 15', 'Laptop HP 15 pulgadas, Intel i5, 8GB RAM', 12999.99, 15, 5, 'laptop-hp.jpg'),
('Mouse Logitech', 'Mouse inalámbrico Logitech M185', 299.99, 50, 10, 'mouse-logitech.jpg'),
('Teclado Mecánico', 'Teclado mecánico RGB para gaming', 1299.99, 20, 5, 'teclado-mecanico.jpg'),
('Monitor Dell 24"', 'Monitor Dell 24 pulgadas Full HD', 3499.99, 10, 3, 'monitor-dell.jpg'),
('Auriculares Sony', 'Auriculares inalámbricos con cancelación de ruido', 2799.99, 25, 8, 'auriculares-sony.jpg'),
('Webcam Logitech HD', 'Webcam Full HD 1080p', 899.99, 30, 10, 'webcam-logitech.jpg'),
('Impresora HP', 'Impresora multifuncional HP DeskJet', 1899.99, 12, 4, 'impresora-hp.jpg'),
('Disco Duro Externo 1TB', 'Disco duro externo portátil 1TB', 1199.99, 40, 15, 'disco-duro.jpg'),
('Cable HDMI 2m', 'Cable HDMI 2.0 de 2 metros', 149.99, 100, 30, 'cable-hdmi.jpg'),
('Hub USB 3.0', 'Hub USB 3.0 de 4 puertos', 349.99, 60, 20, 'hub-usb.jpg');

-- Relacionar productos con proveedores
INSERT INTO AVASTECE (PRODUCTO_id_producto, PROVEEDOR_id_proveedor, fecha_abastecimiento, cantidad) VALUES
(1, 1, NOW(), 0),
(2, 1, NOW(), 0),
(3, 1, NOW(), 0),
(4, 1, NOW(), 0),
(5, 1, NOW(), 0),
(6, 2, NOW(), 0),
(7, 2, NOW(), 0),
(8, 2, NOW(), 0),
(9, 2, NOW(), 0),
(10, 2, NOW(), 0);
