"""
Script para insertar 1000 productos de prueba
"""
from config.database import db
from models.producto import Producto
import random

def generar_productos():
    """Generar 1000 productos de prueba"""
    
    print("Iniciando inserción de 1000 productos...")
    
    # Conectar a la base de datos
    db.connect()
    
    # Categorías de productos
    categorias = [
        'Laptops', 'Monitores', 'Teclados', 'Mouse', 'Auriculares',
        'Webcams', 'Impresoras', 'Discos Duros', 'Cables', 'Hubs',
        'Memorias USB', 'Tarjetas SD', 'Adaptadores', 'Cargadores',
        'Bocinas', 'Microfonos', 'Sillas', 'Escritorios', 'Lamparas',
        'Organizadores'
    ]
    
    marcas = [
        'HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Samsung', 'LG',
        'Logitech', 'Razer', 'Corsair', 'Sony', 'Kingston', 'SanDisk',
        'Western Digital', 'Seagate', 'Canon', 'Epson', 'Microsoft',
        'Apple', 'Xiaomi'
    ]
    
    modelos = [
        'Pro', 'Ultra', 'Plus', 'Max', 'Premium', 'Elite', 'Standard',
        'Basic', 'Advanced', 'Gaming', 'Professional', 'Series', 'Edition',
        'HD', 'RGB', '2024', 'X', 'Air', 'Lite', 'Mini'
    ]
    
    count = 0
    batch_size = 100
    
    for i in range(1, 1001):
        categoria = random.choice(categorias)
        marca = random.choice(marcas)
        modelo = random.choice(modelos)
        
        producto = {
            'nombre': f'{marca} {categoria} {modelo} #{i}',
            'descripcion': f'{categoria} de alta calidad marca {marca} modelo {modelo}',
            'precio': round(random.uniform(99.99, 19999.99), 2),
            'stock': random.randint(0, 200),
            'nivel_minimo': random.randint(5, 30),
            'imagen': f'{categoria.lower()}-{i}.jpg'
        }
        
        Producto.crear(producto)
        count += 1
        
        if count % batch_size == 0:
            print(f"✅ {count} productos creados...")
    
    print(f"\n✅ Total: {count} productos insertados correctamente!")
    
    db.disconnect()

if __name__ == '__main__':
    generar_productos()
