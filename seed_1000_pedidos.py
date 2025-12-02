"""
Script para insertar 1000 pedidos de prueba
"""
from config.database import db
import random
from datetime import datetime, timedelta

def generar_pedidos():
    """Generar 1000 pedidos de prueba"""
    
    print("Iniciando inserción de 1000 pedidos...")
    
    # Conectar a la base de datos
    db.connect()
    
    # Estados posibles
    estados = ['Pendiente', 'Procesando', 'Enviado', 'Entregado', 'Cancelado']
    
    # IDs de usuarios (admin, trabajador, proveedor)
    usuarios = [1, 2, 3]
    
    count = 0
    batch_size = 100
    
    # Fecha inicial (hace 1 año)
    fecha_inicio = datetime.now() - timedelta(days=365)
    
    for i in range(1, 1001):
        # Generar fecha aleatoria en el último año
        dias_aleatorios = random.randint(0, 365)
        fecha_pedido = fecha_inicio + timedelta(days=dias_aleatorios)
        
        # Datos del pedido
        total = round(random.uniform(100.00, 10000.00), 2)
        estado = random.choice(estados)
        id_usuario = random.choice(usuarios)
        procesado_por = random.choice([1, 2])  # Admin o trabajador
        
        query = """
            INSERT INTO PEDIDO (total, estado, fecha, id_usuario, procesado_por)
            VALUES (%s, %s, %s, %s, %s)
        """
        
        db.execute_query(query, (total, estado, fecha_pedido, id_usuario, procesado_por))
        count += 1
        
        if count % batch_size == 0:
            print(f"✅ {count} pedidos creados...")
    
    print(f"\n✅ Total: {count} pedidos insertados correctamente!")
    
    db.disconnect()

if __name__ == '__main__':
    generar_pedidos()
