"""
Configuración de conexión a la base de datos MySQL
Sistema de Comercio Electrónico - Fase 2
"""
import pymysql
import os

class Database:
    def __init__(self):
        self.host = os.getenv('DB_HOST', 'localhost')
        self.user = os.getenv('DB_USER', 'root')
        self.password = os.getenv('DB_PASSWORD', '')
        self.database = os.getenv('DB_NAME', 'ecommerce_db')
        self.connection = None
    
    def connect(self):
        """Establece conexión con la base de datos"""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Conexión exitosa a la base de datos")
            return self.connection
        except Exception as e:
            print(f"Error al conectar a MySQL: {e}")
            return None
    
    def disconnect(self):
        """Cierra la conexión con la base de datos"""
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")
    
    def execute_query(self, query, params=None):
        """Ejecuta una consulta SQL (INSERT, UPDATE, DELETE)"""
        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                self.connection.commit()
                last_id = cursor.lastrowid
                print(f"[DEBUG DB] Query ejecutado exitosamente. LastRowID: {last_id}")
                return last_id
        except Exception as e:
            print(f"[ERROR DB] Error ejecutando query: {e}")
            print(f"[ERROR DB] Query: {query}")
            print(f"[ERROR DB] Params: {params}")
            import traceback
            traceback.print_exc()
            if self.connection:
                self.connection.rollback()
            return None
    
    def fetch_query(self, query, params=None):
        """Ejecuta una consulta SELECT y retorna los resultados"""
        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            print(f"Error en fetch query: {e}")
            return []
    
    def fetch_one(self, query, params=None):
        """Ejecuta una consulta SELECT y retorna un solo resultado"""
        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchone()
        except Exception as e:
            print(f"Error en fetch one: {e}")
            return None

# Instancia global de la base de datos
db = Database()
