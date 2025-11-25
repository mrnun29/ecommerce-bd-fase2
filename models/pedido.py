"""
Modelo Pedido
Gestiona pedidos, carritos de compra y pagos
"""
from config.database import db
from datetime import datetime

class Pedido:
    
    @staticmethod
    def crear(id_cliente, productos):
        """
        Crear un nuevo pedido con productos
        productos: lista de dict con {id_producto, cantidad, precio_unitario}
        """
        try:
            # Calcular total
            total = sum(p['cantidad'] * p['precio_unitario'] for p in productos)
            
            # Crear pedido
            query_pedido = """
                INSERT INTO PEDIDO (total, fecha, estado, id_cliente)
                VALUES (%s, %s, %s, %s)
            """
            id_pedido = db.execute_query(query_pedido, (
                total,
                datetime.now(),
                'Pendiente',
                id_cliente
            ))
            
            if not id_pedido:
                return False
            
            # Agregar productos al carrito
            query_carrito = """
                INSERT INTO CARRITO (PRODUCTO_id_producto, PEDIDO_id_pedido, cantidad, precio_unitario)
                VALUES (%s, %s, %s, %s)
            """
            
            for producto in productos:
                db.execute_query(query_carrito, (
                    producto['id_producto'],
                    id_pedido,
                    producto['cantidad'],
                    producto['precio_unitario']
                ))
                
                # Descontar del stock
                query_stock = """
                    UPDATE PRODUCTO
                    SET stock = stock - %s
                    WHERE id_producto = %s
                """
                db.execute_query(query_stock, (
                    producto['cantidad'],
                    producto['id_producto']
                ))
            
            return id_pedido
        except Exception as e:
            print(f"Error creando pedido: {e}")
            return False
    
    @staticmethod
    def obtener_por_id(id_pedido):
        """Obtener pedido con sus detalles"""
        query = """
            SELECT p.*, c.nombre as cliente_nombre
            FROM PEDIDO p
            JOIN CLIENTE cl ON p.id_cliente = cl.id_cliente
            JOIN USUARIO u ON cl.id_usuario = u.id_usuario
            JOIN (SELECT id_usuario, nombre FROM USUARIO) c ON c.id_usuario = u.id_usuario
            WHERE p.id_pedido = %s
        """
        return db.fetch_one(query, (id_pedido,))
    
    @staticmethod
    def obtener_todos():
        """Obtener todos los pedidos"""
        query = """
            SELECT p.*, u.nombre as cliente_nombre
            FROM PEDIDO p
            JOIN CLIENTE c ON p.id_cliente = c.id_cliente
            JOIN USUARIO u ON c.id_usuario = u.id_usuario
            ORDER BY p.fecha DESC
        """
        return db.fetch_query(query)
    
    @staticmethod
    def obtener_por_cliente(id_cliente):
        """Obtener pedidos de un cliente específico"""
        query = """
            SELECT p.*
            FROM PEDIDO p
            JOIN CLIENTE c ON p.id_cliente = c.id_cliente
            WHERE c.id_usuario = %s
            ORDER BY p.fecha DESC
        """
        return db.fetch_query(query, (id_cliente,))
    
    @staticmethod
    def obtener_productos_pedido(id_pedido):
        """Obtener productos de un pedido"""
        query = """
            SELECT pr.*, c.cantidad, c.precio_unitario,
                   (c.cantidad * c.precio_unitario) as subtotal
            FROM CARRITO c
            JOIN PRODUCTO pr ON c.PRODUCTO_id_producto = pr.id_producto
            WHERE c.PEDIDO_id_pedido = %s
        """
        return db.fetch_query(query, (id_pedido,))
    
    @staticmethod
    def actualizar_estado(id_pedido, nuevo_estado):
        """Actualizar estado del pedido"""
        query = """
            UPDATE PEDIDO
            SET estado = %s
            WHERE id_pedido = %s
        """
        return db.execute_query(query, (nuevo_estado, id_pedido)) is not None
    
    @staticmethod
    def eliminar(id_pedido):
        """Eliminar pedido"""
        query = "DELETE FROM PEDIDO WHERE id_pedido = %s"
        return db.execute_query(query, (id_pedido,)) is not None
    
    @staticmethod
    def obtener_total_ventas_periodo(fecha_inicio, fecha_fin):
        """Calcular total de ventas en un periodo"""
        query = """
            SELECT SUM(total) as total_ventas, COUNT(*) as num_pedidos
            FROM PEDIDO
            WHERE fecha BETWEEN %s AND %s
            AND estado != 'Cancelado'
        """
        return db.fetch_one(query, (fecha_inicio, fecha_fin))
    
    @staticmethod
    def obtener_gasto_promedio_cliente():
        """Calcular gasto promedio por cliente"""
        query = """
            SELECT c.id_cliente, u.nombre, 
                   AVG(p.total) as gasto_promedio,
                   COUNT(p.id_pedido) as num_pedidos
            FROM CLIENTE c
            JOIN USUARIO u ON c.id_usuario = u.id_usuario
            LEFT JOIN PEDIDO p ON c.id_cliente = p.id_cliente
            GROUP BY c.id_cliente
            ORDER BY gasto_promedio DESC
        """
        return db.fetch_query(query)


class Pago:
    
    @staticmethod
    def crear(id_pedido, monto, tipo_pago, detalles_pago):
        """
        Crear un pago para un pedido
        tipo_pago: 'Tarjeta', 'Transferencia', 'Efectivo'
        detalles_pago: dict con información específica según tipo
        """
        try:
            # Crear registro de pago
            query_pago = """
                INSERT INTO PAGO (fecha, monto, tipo_pago, id_pedido)
                VALUES (%s, %s, %s, %s)
            """
            id_pago = db.execute_query(query_pago, (
                datetime.now(),
                monto,
                tipo_pago,
                id_pedido
            ))
            
            if not id_pago:
                return False
            
            # Crear registro específico según tipo de pago
            if tipo_pago == 'Tarjeta':
                query = """
                    INSERT INTO TARJETA (num_tarjeta, banco, vencimiento, cuenta, id_pago)
                    VALUES (%s, %s, %s, %s, %s)
                """
                db.execute_query(query, (
                    detalles_pago['num_tarjeta'],
                    detalles_pago['banco'],
                    detalles_pago['vencimiento'],
                    detalles_pago['cuenta'],
                    id_pago
                ))
            
            elif tipo_pago == 'Transferencia':
                query = """
                    INSERT INTO TRANSFERENCIA (referencia, id_pago)
                    VALUES (%s, %s)
                """
                db.execute_query(query, (
                    detalles_pago['referencia'],
                    id_pago
                ))
            
            elif tipo_pago == 'Efectivo':
                query = """
                    INSERT INTO EFECTIVO (folio, fecha_limite, id_pago)
                    VALUES (%s, %s, %s)
                """
                db.execute_query(query, (
                    detalles_pago['folio'],
                    detalles_pago['fecha_limite'],
                    id_pago
                ))
            
            return id_pago
        except Exception as e:
            print(f"Error creando pago: {e}")
            return False
    
    @staticmethod
    def obtener_por_pedido(id_pedido):
        """Obtener información de pago de un pedido"""
        query = """
            SELECT * FROM PAGO
            WHERE id_pedido = %s
        """
        return db.fetch_one(query, (id_pedido,))
