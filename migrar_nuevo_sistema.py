"""
Script para migrar al nuevo sistema sin clientes
Crea 3 usuarios: Administrador, Trabajador, Proveedor
"""
import mysql.connector
from werkzeug.security import generate_password_hash
from datetime import datetime

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'ecommerce_user',
    'password': 'ecommerce_pass',
    'database': 'ecommerce_db'
}

def ejecutar_sql_file(cursor, filename):
    """Ejecutar un archivo SQL"""
    with open(filename, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    
    # Separar por statements (simple, puede no funcionar con procedures)
    statements = [s.strip() for s in sql_script.split(';') if s.strip() and not s.strip().startswith('--')]
    
    for statement in statements:
        if statement:
            try:
                cursor.execute(statement)
            except Exception as e:
                print(f"Error ejecutando: {statement[:50]}...")
                print(f"Error: {e}")

def main():
    print("🔄 Iniciando migración al nuevo sistema...")
    
    try:
        # Conectar a la base de datos
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        print("✅ Conectado a la base de datos")
        
        # Aplicar nuevo esquema
        print("\n📋 Aplicando nuevo esquema...")
        ejecutar_sql_file(cursor, 'schema_nuevo.sql')
        conn.commit()
        print("✅ Esquema actualizado")
        
        # Generar passwords hasheadas
        admin_pass = generate_password_hash('admin123')
        trabajador_pass = generate_password_hash('trabajador123')
        proveedor_pass = generate_password_hash('proveedor123')
        
        print("\n👥 Creando usuarios...")
        
        # Insertar direcciones
        cursor.execute("""
            INSERT INTO DIRECCION (calle, numero, ciudad, codigo_postal) VALUES
            ('Av. Principal', 100, 'Querétaro', '76000'),
            ('Calle Comercio', 200, 'Querétaro', '76010'),
            ('Blvd. Proveedores', 300, 'Querétaro', '76020')
        """)
        
        # Insertar usuarios
        cursor.execute("""
            INSERT INTO USUARIO (nombre, correo, password, rol, id_direccion) VALUES
            ('Admin Principal', 'admin@sistema.com', %s, 'Administrador', 1),
            ('Trabajador Ventas', 'trabajador@sistema.com', %s, 'Trabajador', 2),
            ('Proveedor Principal', 'proveedor@sistema.com', %s, 'Proveedor', 3)
        """, (admin_pass, trabajador_pass, proveedor_pass))
        
        print("✅ Usuarios creados:")
        print("   - Administrador: admin@sistema.com / admin123")
        print("   - Trabajador: trabajador@sistema.com / trabajador123")
        print("   - Proveedor: proveedor@sistema.com / proveedor123")
        
        # Insertar proveedores
        print("\n🏢 Creando proveedores...")
        cursor.execute("""
            INSERT INTO PROVEEDOR (contacto, empresa, id_direccion, id_usuario) VALUES
            ('Juan Pérez', 'Distribuidora Nacional', 3, 3),
            ('María López', 'Importadora Global', 3, NULL)
        """)
        print("✅ Proveedores creados")
        
        # Insertar productos
        print("\n📦 Creando productos...")
        productos = [
            ('Laptop Dell XPS 15', 'Laptop de alta gama para trabajo profesional', 25999.00, 15, 5, 'https://via.placeholder.com/300x200?text=Laptop'),
            ('Mouse Logitech MX', 'Mouse inalámbrico ergonómico', 899.00, 50, 10, 'https://via.placeholder.com/300x200?text=Mouse'),
            ('Teclado Mecánico RGB', 'Teclado mecánico con iluminación RGB', 1599.00, 30, 8, 'https://via.placeholder.com/300x200?text=Teclado'),
            ('Monitor LG 27"', 'Monitor 4K UHD 27 pulgadas', 6499.00, 8, 5, 'https://via.placeholder.com/300x200?text=Monitor'),
            ('Webcam HD Logitech', 'Cámara web Full HD con micrófono', 1299.00, 25, 10, 'https://via.placeholder.com/300x200?text=Webcam'),
            ('Audífonos Sony WH', 'Audífonos con cancelación de ruido', 4999.00, 3, 5, 'https://via.placeholder.com/300x200?text=Audifonos'),
            ('Hub USB-C 7 puertos', 'Hub multipuertos USB-C', 899.00, 40, 15, 'https://via.placeholder.com/300x200?text=Hub'),
            ('SSD Samsung 1TB', 'Disco de estado sólido 1TB NVMe', 1899.00, 12, 8, 'https://via.placeholder.com/300x200?text=SSD'),
            ('Cable HDMI 4K', 'Cable HDMI 2.1 soporte 4K@120Hz', 299.00, 60, 20, 'https://via.placeholder.com/300x200?text=Cable'),
            ('Mousepad Gaming XXL', 'Mousepad grande para gaming RGB', 499.00, 35, 10, 'https://via.placeholder.com/300x200?text=Mousepad')
        ]
        
        cursor.executemany("""
            INSERT INTO PRODUCTO (nombre, descripcion, precio, stock, nivel_minimo, imagen)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, productos)
        print(f"✅ {len(productos)} productos creados")
        
        # Insertar ventas de ejemplo
        print("\n💰 Creando ventas de ejemplo...")
        cursor.execute("""
            INSERT INTO VENTA (total, metodo_pago, id_trabajador, notas) VALUES
            (26898.00, 'Tarjeta', 2, 'Cliente corporativo - Empresa TechCorp'),
            (2498.00, 'Efectivo', 2, 'Venta de mostrador'),
            (8098.00, 'Transferencia', 2, 'Pedido especial')
        """)
        
        # Insertar detalles de ventas
        cursor.execute("""
            INSERT INTO DETALLE_VENTA (id_venta, id_producto, cantidad, precio_unitario, subtotal) VALUES
            (1, 1, 1, 25999.00, 25999.00),
            (1, 2, 1, 899.00, 899.00),
            (2, 3, 1, 1599.00, 1599.00),
            (2, 2, 1, 899.00, 899.00),
            (3, 4, 1, 6499.00, 6499.00),
            (3, 3, 1, 1599.00, 1599.00)
        """)
        print("✅ Ventas de ejemplo creadas")
        
        # Insertar abastecimientos
        print("\n📥 Registrando abastecimientos...")
        cursor.execute("""
            INSERT INTO AVASTECE (PRODUCTO_id_producto, PROVEEDOR_id_proveedor, cantidad) VALUES
            (1, 1, 20),
            (2, 1, 50),
            (3, 1, 30),
            (4, 2, 15),
            (5, 2, 25),
            (6, 1, 10)
        """)
        print("✅ Abastecimientos registrados")
        
        conn.commit()
        
        print("\n" + "="*60)
        print("✨ ¡Migración completada exitosamente!")
        print("="*60)
        print("\n📝 Credenciales de acceso:")
        print("\n🔐 ADMINISTRADOR:")
        print("   Email: admin@sistema.com")
        print("   Password: admin123")
        print("\n👨‍💼 TRABAJADOR:")
        print("   Email: trabajador@sistema.com")
        print("   Password: trabajador123")
        print("\n🚚 PROVEEDOR:")
        print("   Email: proveedor@sistema.com")
        print("   Password: proveedor123")
        print("\n" + "="*60)
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"\n❌ Error durante la migración: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
