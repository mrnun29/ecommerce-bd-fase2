"""
Modelo Pedido
Gestiona pedidos, carritos de compra y pagos
"""
from config.database import db
from datetime import datetime

class Pedido:
    
    @staticmethod
    def crear(id_usuario, productos, procesado_por=None):
        """
        Crear un nuevo pedido con productos
        id_usuario: usuario para quien se crea el pedido
        productos: lista de dict con {id_producto, cantidad, precio_unitario}
        procesado_por: id del trabajador que procesa el pedido (opcional)
        """
        try:
            # Validar stock disponible antes de crear el pedido
            from models.producto import Producto
            for producto in productos:
                producto_actual = Producto.obtener_por_id(producto['id_producto'])
                if not producto_actual:
                    print(f"Error: Producto {producto['id_producto']} no encontrado")
                    return False
                if producto_actual['stock'] < producto['cantidad']:
                    print(f"Error: Stock insuficiente para {producto_actual['nombre']}. Disponible: {producto_actual['stock']}, Solicitado: {producto['cantidad']}")
                    return False
            
            # Calcular total
            total = sum(p['cantidad'] * p['precio_unitario'] for p in productos)
            
            # Crear pedido
            query_pedido = """
                INSERT INTO PEDIDO (total, fecha, estado, id_usuario, procesado_por)
                VALUES (%s, %s, %s, %s, %s)
            """
            id_pedido = db.execute_query(query_pedido, (
                total,
                datetime.now(),
                'Pendiente',
                id_usuario,
                procesado_por
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
            SELECT p.*, u.nombre as cliente_nombre, 
                   t.nombre as trabajador_nombre
            FROM PEDIDO p
            JOIN USUARIO u ON p.id_usuario = u.id_usuario
            LEFT JOIN USUARIO t ON p.procesado_por = t.id_usuario
            WHERE p.id_pedido = %s
        """
        return db.fetch_one(query, (id_pedido,))
    
    @staticmethod
    def obtener_todos():
        """Obtener todos los pedidos"""
        query = """
            SELECT p.*, u.nombre as cliente_nombre,
                   t.nombre as trabajador_nombre
            FROM PEDIDO p
            JOIN USUARIO u ON p.id_usuario = u.id_usuario
            LEFT JOIN USUARIO t ON p.procesado_por = t.id_usuario
            ORDER BY p.fecha DESC
        """
        return db.fetch_query(query)
    
    @staticmethod
    def obtener_por_usuario(id_usuario):
        """Obtener pedidos de un usuario específico"""
        query = """
            SELECT p.*, t.nombre as trabajador_nombre
            FROM PEDIDO p
            LEFT JOIN USUARIO t ON p.procesado_por = t.id_usuario
            WHERE p.id_usuario = %s
            ORDER BY p.fecha DESC
        """
        return db.fetch_query(query, (id_usuario,))
    
    @staticmethod
    def obtener_por_trabajador(id_trabajador):
        """Obtener pedidos procesados por un trabajador específico"""
        query = """
            SELECT p.*, u.nombre as cliente_nombre
            FROM PEDIDO p
            JOIN USUARIO u ON p.id_usuario = u.id_usuario
            WHERE p.procesado_por = %s
            ORDER BY p.fecha DESC
        """
        return db.fetch_query(query, (id_trabajador,))
    
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
        # Si se está cancelando, devolver stock
        if nuevo_estado == 'Cancelado':
            return Pedido.cancelar(id_pedido)
        
        query = """
            UPDATE PEDIDO
            SET estado = %s
            WHERE id_pedido = %s
        """
        return db.execute_query(query, (nuevo_estado, id_pedido)) is not None
    
    @staticmethod
    def cancelar(id_pedido):
        """Cancelar pedido y devolver stock de los productos"""
        try:
            # Verificar que el pedido existe y no está ya cancelado
            pedido = Pedido.obtener_por_id(id_pedido)
            if not pedido:
                print(f"Error: Pedido {id_pedido} no encontrado")
                return False
            
            if pedido['estado'] == 'Cancelado':
                print(f"Error: Pedido {id_pedido} ya está cancelado")
                return False
            
            # Obtener productos del pedido
            productos = Pedido.obtener_productos_pedido(id_pedido)
            
            # Devolver stock de cada producto
            for item in productos:
                query_stock = """
                    UPDATE PRODUCTO
                    SET stock = stock + %s
                    WHERE id_producto = %s
                """
                db.execute_query(query_stock, (
                    item['cantidad'],
                    item['id_producto']
                ))
                print(f"Stock devuelto: {item['cantidad']} unidades de {item['nombre']}")
            
            # Actualizar estado del pedido a Cancelado
            query = """
                UPDATE PEDIDO
                SET estado = 'Cancelado'
                WHERE id_pedido = %s
            """
            return db.execute_query(query, (id_pedido,)) is not None
        except Exception as e:
            print(f"Error cancelando pedido: {e}")
            return False
    
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
    def obtener_estadisticas_ventas():
        """Obtener estadísticas de ventas"""
        query = """
            SELECT u.id_usuario, u.nombre,
                   COUNT(p.id_pedido) as num_pedidos,
                   SUM(p.total) as total_gastado,
                   AVG(p.total) as gasto_promedio
            FROM USUARIO u
            LEFT JOIN PEDIDO p ON u.id_usuario = p.id_usuario
            WHERE p.estado != 'Cancelado' OR p.estado IS NULL
            GROUP BY u.id_usuario
            ORDER BY total_gastado DESC
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
