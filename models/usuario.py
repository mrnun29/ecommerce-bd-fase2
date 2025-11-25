"""
Modelo Usuario
Gestiona operaciones CRUD para usuarios, direcciones y teléfonos
"""
from config.database import db

class Usuario:
    
    @staticmethod
    def crear(datos):
        """Crear un nuevo usuario con su dirección"""
        try:
            # Primero crear la dirección
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
            
            # Luego crear el usuario
            query_usuario = """
                INSERT INTO USUARIO (nombre, correo, password, rol, id_direccion)
                VALUES (%s, %s, %s, %s, %s)
            """
            id_usuario = db.execute_query(query_usuario, (
                datos['nombre'],
                datos['correo'],
                datos['password'],
                datos.get('rol', 'Cliente'),
                id_direccion
            ))
            
            # Si es cliente, crear registro en tabla CLIENTE
            if id_usuario and datos.get('rol', 'Cliente') == 'Cliente':
                query_cliente = """
                    INSERT INTO CLIENTE (id_usuario, historial_compras)
                    VALUES (%s, %s)
                """
                db.execute_query(query_cliente, (id_usuario, ''))
            
            return id_usuario
        except Exception as e:
            print(f"Error creando usuario: {e}")
            return False
    
    @staticmethod
    def buscar_por_correo(correo):
        """Buscar usuario por correo electrónico"""
        query = """
            SELECT u.*, d.calle, d.numero, d.ciudad, d.codigo_postal
            FROM USUARIO u
            JOIN DIRECCION d ON u.id_direccion = d.id_direccion
            WHERE u.correo = %s
        """
        return db.fetch_one(query, (correo,))
    
    @staticmethod
    def obtener_por_id(id_usuario):
        """Obtener usuario por ID"""
        query = """
            SELECT u.*, d.calle, d.numero, d.ciudad, d.codigo_postal
            FROM USUARIO u
            JOIN DIRECCION d ON u.id_direccion = d.id_direccion
            WHERE u.id_usuario = %s
        """
        return db.fetch_one(query, (id_usuario,))
    
    @staticmethod
    def obtener_todos():
        """Obtener todos los usuarios"""
        query = """
            SELECT u.*, d.calle, d.numero, d.ciudad, d.codigo_postal
            FROM USUARIO u
            JOIN DIRECCION d ON u.id_direccion = d.id_direccion
            ORDER BY u.id_usuario DESC
        """
        return db.fetch_query(query)
    
    @staticmethod
    def actualizar(id_usuario, datos):
        """Actualizar información del usuario"""
        try:
            # Actualizar dirección
            query_direccion = """
                UPDATE DIRECCION d
                JOIN USUARIO u ON d.id_direccion = u.id_direccion
                SET d.calle = %s, d.numero = %s, d.ciudad = %s, d.codigo_postal = %s
                WHERE u.id_usuario = %s
            """
            db.execute_query(query_direccion, (
                datos['calle'],
                datos.get('numero'),
                datos['ciudad'],
                datos['codigo_postal'],
                id_usuario
            ))
            
            # Actualizar usuario
            query_usuario = """
                UPDATE USUARIO
                SET nombre = %s, correo = %s, rol = %s
                WHERE id_usuario = %s
            """
            db.execute_query(query_usuario, (
                datos['nombre'],
                datos['correo'],
                datos['rol'],
                id_usuario
            ))
            
            return True
        except Exception as e:
            print(f"Error actualizando usuario: {e}")
            return False
    
    @staticmethod
    def eliminar(id_usuario):
        """Eliminar usuario"""
        query = "DELETE FROM USUARIO WHERE id_usuario = %s"
        return db.execute_query(query, (id_usuario,)) is not None
    
    @staticmethod
    def agregar_telefono(id_usuario, numero_telefono):
        """Agregar teléfono a un usuario"""
        query = """
            INSERT INTO TELEFONO (telefono, id_usuario)
            VALUES (%s, %s)
        """
        return db.execute_query(query, (numero_telefono, id_usuario))
    
    @staticmethod
    def obtener_telefonos(id_usuario):
        """Obtener todos los teléfonos de un usuario"""
        query = """
            SELECT * FROM TELEFONO
            WHERE id_usuario = %s
        """
        return db.fetch_query(query, (id_usuario,))
