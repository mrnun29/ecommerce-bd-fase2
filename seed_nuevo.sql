-- Datos iniciales para Sistema de Gestión de Inventario
-- 3 Usuarios: Administrador, Trabajador, Proveedor

USE `ecommerce_db`;

-- Insertar direcciones
INSERT INTO `DIRECCION` (`calle`, `numero`, `ciudad`, `codigo_postal`) VALUES
('Av. Principal', 100, 'Querétaro', '76000'),
('Calle Comercio', 200, 'Querétaro', '76010'),
('Blvd. Proveedores', 300, 'Querétaro', '76020');

-- Insertar usuarios (contraseñas hasheadas con werkzeug: "admin123", "trabajador123", "proveedor123")
INSERT INTO `USUARIO` (`nombre`, `correo`, `password`, `rol`, `id_direccion`) VALUES
-- Administrador
('Admin Principal', 'admin@sistema.com', 'scrypt:32768:8:1$K0zGsT9yDPcqNaGk$dfc4c3bc5e6e7b0d4f8a9b2c1d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e', 'Administrador', 1),
-- Trabajador
('Trabajador Ventas', 'trabajador@sistema.com', 'scrypt:32768:8:1$K0zGsT9yDPcqNaGk$dfc4c3bc5e6e7b0d4f8a9b2c1d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e', 'Trabajador', 2),
-- Proveedor
('Proveedor Principal', 'proveedor@sistema.com', 'scrypt:32768:8:1$K0zGsT9yDPcqNaGk$dfc4c3bc5e6e7b0d4f8a9b2c1d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e', 'Proveedor', 3);

-- Insertar proveedores
INSERT INTO `PROVEEDOR` (`contacto`, `empresa`, `id_direccion`, `id_usuario`) VALUES
('Juan Pérez', 'Distribuidora Nacional', 3, 3),
('María López', 'Importadora Global', 3, NULL);

-- Insertar productos
INSERT INTO `PRODUCTO` (`nombre`, `descripcion`, `precio`, `stock`, `nivel_minimo`, `imagen`) VALUES
('Laptop Dell XPS 15', 'Laptop de alta gama para trabajo profesional', 25999.00, 15, 5, 'https://via.placeholder.com/300x200?text=Laptop'),
('Mouse Logitech MX', 'Mouse inalámbrico ergonómico', 899.00, 50, 10, 'https://via.placeholder.com/300x200?text=Mouse'),
('Teclado Mecánico RGB', 'Teclado mecánico con iluminación RGB', 1599.00, 30, 8, 'https://via.placeholder.com/300x200?text=Teclado'),
('Monitor LG 27"', 'Monitor 4K UHD 27 pulgadas', 6499.00, 8, 5, 'https://via.placeholder.com/300x200?text=Monitor'),
('Webcam HD Logitech', 'Cámara web Full HD con micrófono', 1299.00, 25, 10, 'https://via.placeholder.com/300x200?text=Webcam'),
('Audífonos Sony WH', 'Audífonos con cancelación de ruido', 4999.00, 3, 5, 'https://via.placeholder.com/300x200?text=Audifonos'),
('Hub USB-C 7 puertos', 'Hub multipuertos USB-C', 899.00, 40, 15, 'https://via.placeholder.com/300x200?text=Hub'),
('SSD Samsung 1TB', 'Disco de estado sólido 1TB NVMe', 1899.00, 12, 8, 'https://via.placeholder.com/300x200?text=SSD'),
('Cable HDMI 4K', 'Cable HDMI 2.1 soporte 4K@120Hz', 299.00, 60, 20, 'https://via.placeholder.com/300x200?text=Cable'),
('Mousepad Gaming XXL', 'Mousepad grande para gaming RGB', 499.00, 35, 10, 'https://via.placeholder.com/300x200?text=Mousepad');

-- Insertar algunas ventas de ejemplo
INSERT INTO `VENTA` (`total`, `metodo_pago`, `id_trabajador`, `notas`) VALUES
(26898.00, 'Tarjeta', 2, 'Cliente corporativo - Empresa TechCorp'),
(2498.00, 'Efectivo', 2, 'Venta de mostrador'),
(8098.00, 'Transferencia', 2, 'Pedido especial - Monitor + Teclado + Mouse');

-- Insertar detalles de ventas
INSERT INTO `DETALLE_VENTA` (`id_venta`, `id_producto`, `cantidad`, `precio_unitario`, `subtotal`) VALUES
(1, 1, 1, 25999.00, 25999.00),
(1, 2, 1, 899.00, 899.00),
(2, 3, 1, 1599.00, 1599.00),
(2, 2, 1, 899.00, 899.00),
(3, 4, 1, 6499.00, 6499.00),
(3, 3, 1, 1599.00, 1599.00);

-- Insertar algunos abastecimientos
INSERT INTO `AVASTECE` (`PRODUCTO_id_producto`, `PROVEEDOR_id_proveedor`, `cantidad`) VALUES
(1, 1, 20),
(2, 1, 50),
(3, 1, 30),
(4, 2, 15),
(5, 2, 25),
(6, 1, 10);
