"""Script para crear un usuario administrador"""
from werkzeug.security import generate_password_hash
from config.database import db
from models.usuario import Usuario

db.connect()

# Datos del nuevo usuario
nuevo_usuario = {
    'nombre': 'Nuevo Admin',
    'correo': 'nuevo@admin.com',
    'password': generate_password_hash('password123'),
    'rol': 'Administrador',  # Cambiar a 'Empleado' o 'Cliente'
    'calle': 'Mi Calle',
    'numero': 123,
    'ciudad': 'Querétaro',
    'codigo_postal': '76000'
}

if Usuario.crear(nuevo_usuario):
    print(f"✅ Usuario {nuevo_usuario['correo']} creado exitosamente!")
    print(f"   Rol: {nuevo_usuario['rol']}")
else:
    print("❌ Error al crear usuario")

db.disconnect()
