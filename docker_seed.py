"""
Script para insertar datos de prueba en Docker
"""
import time
from werkzeug.security import generate_password_hash
from config.database import db
from models.usuario import Usuario
from models.producto import Producto
from models.proveedor import Proveedor

def wait_for_db():
    """Esperar a que MySQL esté listo"""
    max_retries = 30
    for i in range(max_retries):
        try:
            db.connect()
            print("✅ Conexión a MySQL exitosa")
            return True
        except Exception as e:
            print(f"Esperando MySQL... ({i+1}/{max_retries})")
            time.sleep(2)
    return False

def seed_database():
    """Insertar datos de prueba"""
    print("\n🌱 Iniciando inserción de datos...")
    
    if not wait_for_db():
        print("❌ No se pudo conectar a MySQL")
        return
    
    try:
        # Crear usuarios
        print("\n👥 Creando usuarios...")
        admin_data = {
            'nombre': 'Admin Principal',
            'correo': 'admin@ecommerce.com',
            'password': generate_password_hash('admin123'),
            'rol': 'Administrador',
            'calle': 'Av. Principal',
            'numero': 100,
            'ciudad': 'Querétaro',
            'codigo_postal': '76000'
        }
        Usuario.crear(admin_data)
        
        empleado_data = {
            'nombre': 'Juan Empleado',
            'correo': 'empleado@ecommerce.com',
            'password': generate_password_hash('empleado123'),
            'rol': 'Empleado',
            'calle': 'Calle Trabajo',
            'numero': 50,
            'ciudad': 'Querétaro',
            'codigo_postal': '76010'
        }
        Usuario.crear(empleado_data)
        
        cliente_data = {
            'nombre': 'María Cliente',
            'correo': 'cliente@email.com',
            'password': generate_password_hash('cliente123'),
            'rol': 'Cliente',
            'calle': 'Calle Residencial',
            'numero': 25,
            'ciudad': 'Querétaro',
            'codigo_postal': '76020'
        }
        Usuario.crear(cliente_data)
        print("✅ Usuarios creados")
        
        # Crear proveedores
        print("\n🏭 Creando proveedores...")
        proveedor1 = {
            'contacto': 'Carlos López',
            'empresa': 'Distribuidora Tech SA',
            'calle': 'Zona Industrial',
            'numero': 500,
            'ciudad': 'Querétaro',
            'codigo_postal': '76120'
        }
        Proveedor.crear(proveedor1)
        
        proveedor2 = {
            'contacto': 'Ana García',
            'empresa': 'Importaciones Global',
            'calle': 'Parque Industrial',
            'numero': 300,
            'ciudad': 'Querétaro',
            'codigo_postal': '76130'
        }
        Proveedor.crear(proveedor2)
        print("✅ Proveedores creados")
        
        # Crear productos
        print("\n📦 Creando productos...")
        productos = [
            {'nombre': 'Laptop HP 15', 'descripcion': 'Laptop HP 15 pulgadas, Intel i5, 8GB RAM', 'precio': 12999.99, 'stock': 15, 'nivel_minimo': 5},
            {'nombre': 'Mouse Logitech', 'descripcion': 'Mouse inalámbrico Logitech M185', 'precio': 299.99, 'stock': 50, 'nivel_minimo': 10},
            {'nombre': 'Teclado Mecánico', 'descripcion': 'Teclado mecánico RGB para gaming', 'precio': 1299.99, 'stock': 20, 'nivel_minimo': 5},
            {'nombre': 'Monitor Dell 24"', 'descripcion': 'Monitor Dell 24 pulgadas Full HD', 'precio': 3499.99, 'stock': 10, 'nivel_minimo': 3},
            {'nombre': 'Auriculares Sony', 'descripcion': 'Auriculares inalámbricos', 'precio': 2799.99, 'stock': 25, 'nivel_minimo': 8},
        ]
        
        for producto in productos:
            Producto.crear(producto)
        print(f"✅ {len(productos)} productos creados")
        
        print("\n" + "="*60)
        print("✅ Datos de prueba insertados correctamente!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        db.disconnect()

if __name__ == '__main__':
    seed_database()
