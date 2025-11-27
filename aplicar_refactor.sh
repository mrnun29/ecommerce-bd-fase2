#!/bin/bash

# Script para aplicar la refactorización del sistema
# Sistema de 3 Roles de Usuario

echo "=========================================="
echo "Sistema de E-Commerce - Refactorización"
echo "Aplicando nuevo schema de 3 roles"
echo "=========================================="
echo ""

# Verificar que existe el archivo .env
if [ ! -f .env ]; then
    echo "❌ Error: No se encontró el archivo .env"
    echo "Crea el archivo .env con las credenciales de la base de datos"
    exit 1
fi

# Cargar variables de entorno
source .env

echo "📦 1. Eliminando base de datos anterior..."
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} -e "DROP DATABASE IF EXISTS ${DB_NAME};"

echo "📦 2. Creando nueva base de datos..."
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} -e "CREATE DATABASE ${DB_NAME};"

echo "📦 3. Aplicando nuevo schema..."
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASSWORD} ${DB_NAME} < schema_refactor.sql

echo "📦 4. Insertando datos de prueba..."
python3 seed_refactor.py

echo ""
echo "=========================================="
echo "✅ Refactorización completada!"
echo "=========================================="
echo ""
echo "🔑 Puedes iniciar sesión con:"
echo ""
echo "👨‍💼 Administrador:"
echo "   Email: admin@ecommerce.com"
echo "   Password: admin123"
echo ""
echo "👷 Trabajador:"
echo "   Email: trabajador@ecommerce.com"
echo "   Password: trabajador123"
echo ""
echo "🚚 Proveedor:"
echo "   Email: proveedor@ecommerce.com"
echo "   Password: proveedor123"
echo ""
echo "=========================================="
