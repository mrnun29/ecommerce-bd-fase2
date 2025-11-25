"""
Modelo Producto
Gestiona operaciones CRUD para productos e inventario
"""
from config.database import db

class Producto:
    
    @staticmethod
    def crear(datos):
        """Crear un nuevo producto"""
        query = """
            INSERT INTO PRODUCTO (nombre, descripcion, precio, stock, nivel_minimo, imagen)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        return db.execute_query(query, (
            datos['nombre'],
            datos.get('descripcion'),
            datos['precio'],
            datos.get('stock', 0),
            datos.get('nivel_minimo', 10),
            datos.get('imagen')
        ))
    
    @staticmethod
    def obtener_por_id(id_producto):
        """Obtener producto por ID"""
        query = "SELECT * FROM PRODUCTO WHERE id_producto = %s"
        return db.fetch_one(query, (id_producto,))
    
    @staticmethod
    def obtener_todos():
        """Obtener todos los productos"""
        query = "SELECT * FROM PRODUCTO ORDER BY id_producto DESC"
        return db.fetch_query(query)
    
    @staticmethod
    def actualizar(id_producto, datos):
        """Actualizar un producto"""
        query = """
            UPDATE PRODUCTO
            SET nombre = %s, descripcion = %s, precio = %s, 
                stock = %s, nivel_minimo = %s, imagen = %s
            WHERE id_producto = %s
        """
        return db.execute_query(query, (
            datos['nombre'],
            datos.get('descripcion'),
            datos['precio'],
            datos['stock'],
            datos['nivel_minimo'],
            datos.get('imagen'),
            id_producto
        )) is not None
    
    @staticmethod
    def eliminar(id_producto):
        """Eliminar un producto"""
        query = "DELETE FROM PRODUCTO WHERE id_producto = %s"
        return db.execute_query(query, (id_producto,)) is not None
    
    @staticmethod
    def buscar(termino):
        """Buscar productos por nombre o descripción"""
        query = """
            SELECT * FROM PRODUCTO
            WHERE nombre LIKE %s OR descripcion LIKE %s
            ORDER BY nombre
        """
        patron = f"%{termino}%"
        return db.fetch_query(query, (patron, patron))
    
    @staticmethod
    def obtener_stock_bajo():
        """Obtener productos con stock por debajo del nivel mínimo"""
        query = """
            SELECT * FROM PRODUCTO
            WHERE stock < nivel_minimo
            ORDER BY stock ASC
        """
        return db.fetch_query(query)
    
    @staticmethod
    def actualizar_stock(id_producto, cantidad):
        """Actualizar el stock de un producto"""
        query = """
            UPDATE PRODUCTO
            SET stock = stock + %s
            WHERE id_producto = %s
        """
        return db.execute_query(query, (cantidad, id_producto)) is not None
    
    @staticmethod
    def verificar_disponibilidad(id_producto, cantidad_solicitada):
        """Verificar si hay suficiente stock disponible"""
        producto = Producto.obtener_por_id(id_producto)
        if producto:
            return producto['stock'] >= cantidad_solicitada
        return False
    
    @staticmethod
    def obtener_productos_mas_vendidos(limite=10):
        """Obtener los productos más vendidos"""
        query = """
            SELECT p.*, COUNT(c.PRODUCTO_id_producto) as total_vendido
            FROM PRODUCTO p
            LEFT JOIN CARRITO c ON p.id_producto = c.PRODUCTO_id_producto
            GROUP BY p.id_producto
            ORDER BY total_vendido DESC
            LIMIT %s
        """
        return db.fetch_query(query, (limite,))
    
    @staticmethod
    def obtener_ranking_ingresos(limite=10):
        """Obtener ranking de productos por ingresos generados"""
        query = """
            SELECT p.*, 
                   SUM(c.cantidad * c.precio_unitario) as ingresos_totales,
                   SUM(c.cantidad) as unidades_vendidas
            FROM PRODUCTO p
            LEFT JOIN CARRITO c ON p.id_producto = c.PRODUCTO_id_producto
            GROUP BY p.id_producto
            ORDER BY ingresos_totales DESC
            LIMIT %s
        """
        return db.fetch_query(query, (limite,))
    
    @staticmethod
    def obtener_proveedores(id_producto):
        """Obtener proveedores que abastecen un producto"""
        query = """
            SELECT pr.*, a.fecha_abastecimiento, a.cantidad
            FROM PROVEEDOR pr
            JOIN AVASTECE a ON pr.id_proveedor = a.PROVEEDOR_id_proveedor
            WHERE a.PRODUCTO_id_producto = %s
            ORDER BY a.fecha_abastecimiento DESC
        """
        return db.fetch_query(query, (id_producto,))
