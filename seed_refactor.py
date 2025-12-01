"""
Script para insertar datos de prueba - Sistema Refactorizado
Sistema de Comercio Electrónico con 3 Roles de Usuario
"""
from werkzeug.security import generate_password_hash
from config.database import db
from models.usuario import Usuario
from models.producto import Producto
from models.proveedor import Proveedor

def seed_database():
    """Insertar datos de prueba en la base de datos"""
    
    print("Iniciando inserción de datos de prueba (Sistema Refactorizado)...")
    
    # Conectar a la base de datos
    db.connect()
    
    # 1. Crear usuarios de prueba
    print("\n1. Creando usuarios...")
    
    # Usuario Administrador
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
    id_admin = Usuario.crear(admin_data)
    print("✅ Administrador creado")
    
    # Usuario Trabajador
    trabajador_data = {
        'nombre': 'Juan Trabajador',
        'correo': 'trabajador@ecommerce.com',
        'password': generate_password_hash('trabajador123'),
        'rol': 'Trabajador',
        'calle': 'Calle Trabajo',
        'numero': 50,
        'ciudad': 'Querétaro',
        'codigo_postal': '76010'
    }
    id_trabajador = Usuario.crear(trabajador_data)
    print("✅ Trabajador creado")
    
    # Usuario Proveedor (primero crear la empresa proveedora)
    proveedor_empresa_data = {
        'contacto': 'Carlos López',
        'empresa': 'Distribuidora Tech SA',
        'telefono': '4421234567',
        'calle': 'Zona Industrial',
        'numero': 500,
        'ciudad': 'Querétaro',
        'codigo_postal': '76120'
    }
    id_proveedor_empresa = Proveedor.crear(proveedor_empresa_data)
    
    # Crear usuario tipo Proveedor
    proveedor_usuario_data = {
        'nombre': 'Carlos López',
        'correo': 'proveedor@ecommerce.com',
        'password': generate_password_hash('proveedor123'),
        'rol': 'Proveedor',
        'calle': 'Zona Industrial',
        'numero': 500,
        'ciudad': 'Querétaro',
        'codigo_postal': '76120'
    }
    id_proveedor_usuario = Usuario.crear(proveedor_usuario_data)
    
    # Vincular usuario proveedor con empresa
    if id_proveedor_usuario and id_proveedor_empresa:
        query_vincular = """
            INSERT INTO PROVEEDOR_USUARIO (id_proveedor, id_usuario)
            VALUES (%s, %s)
        """
        db.execute_query(query_vincular, (id_proveedor_empresa, id_proveedor_usuario))
    
    print("✅ Proveedor creado y vinculado")
    
    # 2. Crear más empresas proveedoras
    print("\n2. Creando proveedores adicionales...")
    
    proveedor2 = {
        'contacto': 'Ana García',
        'empresa': 'Importaciones Global',
        'telefono': '4427654321',
        'calle': 'Parque Industrial',
        'numero': 300,
        'ciudad': 'Querétaro',
        'codigo_postal': '76130'
    }
    id_proveedor2 = Proveedor.crear(proveedor2)
    print("✅ Proveedores adicionales creados")
    
    # 3. Crear productos
    print("\n3. Creando productos...")
    
    productos = [
        {
            'nombre': 'Laptop HP 15',
            'descripcion': 'Laptop HP 15 pulgadas, Intel i5, 8GB RAM',
            'precio': 12999.99,
            'stock': 15,
            'nivel_minimo': 5,
            'imagen': 'laptop-hp.jpg'
        },
        {
            'nombre': 'Mouse Logitech',
            'descripcion': 'Mouse inalámbrico Logitech M185',
            'precio': 299.99,
            'stock': 50,
            'nivel_minimo': 10,
            'imagen': 'mouse-logitech.jpg'
        },
        {
            'nombre': 'Teclado Mecánico',
            'descripcion': 'Teclado mecánico RGB para gaming',
            'precio': 1299.99,
            'stock': 20,
            'nivel_minimo': 5,
            'imagen': 'teclado-mecanico.jpg'
        },
        {
            'nombre': 'Monitor Dell 24"',
            'descripcion': 'Monitor Dell 24 pulgadas Full HD',
            'precio': 3499.99,
            'stock': 10,
            'nivel_minimo': 3,
            'imagen': 'monitor-dell.jpg'
        },
        {
            'nombre': 'Auriculares Sony',
            'descripcion': 'Auriculares inalámbricos con cancelación de ruido',
            'precio': 2799.99,
            'stock': 25,
            'nivel_minimo': 8,
            'imagen': 'auriculares-sony.jpg'
        },
        {
            'nombre': 'Webcam Logitech HD',
            'descripcion': 'Webcam Full HD 1080p',
            'precio': 899.99,
            'stock': 30,
            'nivel_minimo': 10,
            'imagen': 'webcam-logitech.jpg'
        },
        {
            'nombre': 'Impresora HP',
            'descripcion': 'Impresora multifuncional HP DeskJet',
            'precio': 1899.99,
            'stock': 12,
            'nivel_minimo': 4,
            'imagen': 'impresora-hp.jpg'
        },
        {
            'nombre': 'Disco Duro Externo 1TB',
            'descripcion': 'Disco duro externo portátil 1TB',
            'precio': 1199.99,
            'stock': 40,
            'nivel_minimo': 15,
            'imagen': 'disco-duro.jpg'
        },
        {
            'nombre': 'Cable HDMI 2m',
            'descripcion': 'Cable HDMI 2.0 de 2 metros',
            'precio': 149.99,
            'stock': 100,
            'nivel_minimo': 30,
            'imagen': 'cable-hdmi.jpg'
        },
        {
            'nombre': 'Hub USB 3.0',
            'descripcion': 'Hub USB 3.0 de 4 puertos',
            'precio': 349.99,
            'stock': 60,
            'nivel_minimo': 20,
            'imagen': 'hub-usb.jpg'
        }
    ]
    
    for producto in productos:
        Producto.crear(producto)
    
    print(f"✅ {len(productos)} productos creados")
    
    # 4. Registrar abastecimientos
    print("\n4. Registrando abastecimientos iniciales...")
    
    # Proveedor 1 abastece productos 1-5
    for i in range(1, 6):
        Proveedor.registrar_abastecimiento(id_proveedor_empresa, i, 0)  # Ya tienen stock inicial
    
    # Proveedor 2 abastece productos 6-10
    for i in range(6, 11):
        Proveedor.registrar_abastecimiento(id_proveedor2, i, 0)  # Ya tienen stock inicial
    
    print("✅ Abastecimientos registrados")
    
    print("\n" + "="*50)
    print("✅ Datos de prueba insertados correctamente!")
    print("="*50)
    print("\n🔑 Credenciales de acceso:")
    print("\n👨‍💼 Administrador:")
    print("  Email: admin@ecommerce.com")
    print("  Password: admin123")
    print("\n👷 Trabajador:")
    print("  Email: trabajador@ecommerce.com")
    print("  Password: trabajador123")
    print("\n🚚 Proveedor:")
    print("  Email: proveedor@ecommerce.com")
    print("  Password: proveedor123")
    print("\n" + "="*50)
    
    db.disconnect()

if __name__ == '__main__':
    seed_database()
