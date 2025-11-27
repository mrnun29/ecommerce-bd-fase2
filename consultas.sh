#!/bin/bash
# Script con consultas útiles para la base de datos

echo "📊 Consultas Rápidas - Base de Datos E-Commerce"
echo "================================================"

# Ver todas las tablas
echo -e "\n🗂️  TABLAS:"
docker-compose exec mysql mysql -u ecommerce_user -pecommerce_pass ecommerce_db -e "SHOW TABLES;"

# Ver usuarios
echo -e "\n👥 USUARIOS:"
docker-compose exec mysql mysql -u ecommerce_user -pecommerce_pass ecommerce_db -e "SELECT id_usuario, nombre, correo, rol FROM USUARIO;"

# Ver productos
echo -e "\n📦 PRODUCTOS:"
docker-compose exec mysql mysql -u ecommerce_user -pecommerce_pass ecommerce_db -e "SELECT id_producto, nombre, precio, stock, nivel_minimo FROM PRODUCTO;"

# Ver proveedores
echo -e "\n🏭 PROVEEDORES:"
docker-compose exec mysql mysql -u ecommerce_user -pecommerce_pass ecommerce_db -e "SELECT id_proveedor, empresa, contacto FROM PROVEEDOR;"

# Ver pedidos
echo -e "\n🛒 PEDIDOS:"
docker-compose exec mysql mysql -u ecommerce_user -pecommerce_pass ecommerce_db -e "SELECT id_pedido, total, fecha, estado FROM PEDIDO;"

# Productos con stock bajo
echo -e "\n⚠️  STOCK BAJO:"
docker-compose exec mysql mysql -u ecommerce_user -pecommerce_pass ecommerce_db -e "SELECT nombre, stock, nivel_minimo FROM PRODUCTO WHERE stock < nivel_minimo;"
