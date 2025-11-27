"""
Modelo Proveedor
Gestiona proveedores y su relación con productos
"""
from config.database import db
from datetime import datetime

class Proveedor:
    
    @staticmethod
    def crear(datos):
        """Crear un nuevo proveedor con su dirección"""
        try:
            # Crear dirección
            query_direccion = """
                INSERT INTO DIRECCION (calle, numero, ciudad, codigo_postal)
                VALUES (%s, %s, %s, %s)
            """
            id_direccion = db.execute_query(query_direccion, (
                datos['calle'],
                datos.get('numero'),
                datos['ciudad'],
                datos['codigo_postal']
            ))
            
            if not id_direccion:
                return False
            
            # Crear proveedor
            query_proveedor = """
                INSERT INTO PROVEEDOR (contacto, empresa, id_direccion)
                VALUES (%s, %s, %s)
            """
            return db.execute_query(query_proveedor, (
                datos['contacto'],
                datos['empresa'],
                id_direccion
            ))
        except Exception as e:
            print(f"Error creando proveedor: {e}")
            return False
    
    @staticmethod
    def obtener_por_id(id_proveedor):
        """Obtener proveedor por ID"""
        query = """
            SELECT p.*, d.calle, d.numero, d.ciudad, d.codigo_postal
            FROM PROVEEDOR p
            JOIN DIRECCION d ON p.id_direccion = d.id_direccion
            WHERE p.id_proveedor = %s
        """
        return db.fetch_one(query, (id_proveedor,))
    
    @staticmethod
    def obtener_todos():
        """Obtener todos los proveedores"""
        query = """
            SELECT p.*, d.calle, d.numero, d.ciudad, d.codigo_postal
            FROM PROVEEDOR p
            JOIN DIRECCION d ON p.id_direccion = d.id_direccion
            ORDER BY p.empresa
        """
        return db.fetch_query(query)
    
    @staticmethod
    def actualizar(id_proveedor, datos):
        """Actualizar proveedor"""
        try:
            # Actualizar dirección
            query_direccion = """
                UPDATE DIRECCION d
                JOIN PROVEEDOR p ON d.id_direccion = p.id_direccion
                SET d.calle = %s, d.numero = %s, d.ciudad = %s, d.codigo_postal = %s
                WHERE p.id_proveedor = %s
            """
            db.execute_query(query_direccion, (
                datos['calle'],
                datos.get('numero'),
                datos['ciudad'],
                datos['codigo_postal'],
                id_proveedor
            ))
            
            # Actualizar proveedor
            query_proveedor = """
                UPDATE PROVEEDOR
                SET contacto = %s, empresa = %s
                WHERE id_proveedor = %s
            """
            db.execute_query(query_proveedor, (
                datos['contacto'],
                datos['empresa'],
                id_proveedor
            ))
            
            return True
        except Exception as e:
            print(f"Error actualizando proveedor: {e}")
            return False
    
    @staticmethod
    def eliminar(id_proveedor):
        """Eliminar proveedor"""
        query = "DELETE FROM PROVEEDOR WHERE id_proveedor = %s"
        return db.execute_query(query, (id_proveedor,)) is not None
    
    @staticmethod
    def registrar_abastecimiento(id_proveedor, id_producto, cantidad):
        """Registrar abastecimiento de producto por proveedor"""
        try:
            # Primero actualizar el stock del producto
            query_stock = """
                UPDATE PRODUCTO
                SET stock = stock + %s
                WHERE id_producto = %s
            """
            stock_result = db.execute_query(query_stock, (cantidad, id_producto))
            print(f"Stock actualizado: producto {id_producto}, cantidad +{cantidad}, result: {stock_result}")
            
            # Luego registrar el abastecimiento en historial
            query = """
                INSERT INTO AVASTECE (PRODUCTO_id_producto, PROVEEDOR_id_proveedor, fecha_abastecimiento, cantidad)
                VALUES (%s, %s, %s, %s)
            """
            result = db.execute_query(query, (
                id_producto,
                id_proveedor,
                datetime.now(),
                cantidad
            ))
            print(f"Abastecimiento registrado: result: {result}")
            
            return stock_result is not None
        except Exception as e:
            print(f"Error registrando abastecimiento: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    @staticmethod
    def abastecer_producto(id_proveedor, id_producto, cantidad):
        """Alias de registrar_abastecimiento para mejor legibilidad"""
        return Proveedor.registrar_abastecimiento(id_proveedor, id_producto, cantidad)
    
    @staticmethod
    def obtener_productos_abastecidos(id_proveedor):
        """Obtener productos que abastece un proveedor"""
        query = """
            SELECT pr.*, a.fecha_abastecimiento, a.cantidad
            FROM PRODUCTO pr
            JOIN AVASTECE a ON pr.id_producto = a.PRODUCTO_id_producto
            WHERE a.PROVEEDOR_id_proveedor = %s
            ORDER BY a.fecha_abastecimiento DESC
        """
        return db.fetch_query(query, (id_proveedor,))
    
    @staticmethod
    def obtener_proveedores_con_usuarios():
        """Obtener todos los proveedores con sus usuarios vinculados"""
        query = """
            SELECT p.id_proveedor, p.contacto, p.empresa,
                   d.calle, d.numero, d.ciudad, d.codigo_postal,
                   u.id_usuario, u.nombre as nombre_usuario, u.correo
            FROM PROVEEDOR p
            JOIN DIRECCION d ON p.id_direccion = d.id_direccion
            LEFT JOIN PROVEEDOR_USUARIO pu ON p.id_proveedor = pu.id_proveedor
            LEFT JOIN USUARIO u ON pu.id_usuario = u.id_usuario
            ORDER BY p.empresa, u.nombre
        """
        return db.fetch_query(query)
