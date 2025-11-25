#!/bin/bash

# Script de configuración rápida del proyecto
# Sistema de Comercio Electrónico - Fase 2

echo "======================================"
echo "Sistema de Comercio Electrónico"
echo "Configuración Inicial"
echo "======================================"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado. Por favor instálalo primero."
    exit 1
fi
echo "✅ Python 3 detectado"

# Verificar MySQL
if ! command -v mysql &> /dev/null; then
    echo "⚠️  MySQL no detectado. Asegúrate de tenerlo instalado."
else
    echo "✅ MySQL detectado"
fi

# Crear entorno virtual
echo ""
echo "📦 Creando entorno virtual..."
python3 -m venv venv

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

# Crear archivo .env si no existe
if [ ! -f .env ]; then
    echo "⚙️  Creando archivo .env..."
    cp .env.example .env
    echo "⚠️  Por favor edita el archivo .env con tus credenciales de MySQL"
fi

echo ""
echo "======================================"
echo "✅ Configuración completada!"
echo "======================================"
echo ""
echo "Próximos pasos:"
echo "1. Editar archivo .env con tus credenciales"
echo "2. Crear la base de datos:"
echo "   mysql -u root -p < schema.sql"
echo "3. Ejecutar la aplicación:"
echo "   python app.py"
echo ""
echo "La aplicación estará en: http://localhost:5000"
echo ""
