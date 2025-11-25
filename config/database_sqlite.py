"""
Configuración de conexión a SQLite (sin contraseña)
Sistema de Comercio Electrónico - Fase 2
"""
import sqlite3
import os

class Database:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ecommerce.db')
        self.connection = None
    
    def connect(self):
        """Establece conexión con la base de datos"""
        try:
            self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
            self.connection.row_factory = sqlite3.Row
            print("Conexión exitosa a la base de datos SQLite")
            return self.connection
        except Exception as e:
            print(f"Error al conectar a SQLite: {e}")
            return None
    
    def disconnect(self):
        """Cierra la conexión con la base de datos"""
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")
    
    def execute_query(self, query, params=None):
        """Ejecuta una consulta SQL (INSERT, UPDATE, DELETE)"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error ejecutando query: {e}")
            self.connection.rollback()
            return None
    
    def fetch_query(self, query, params=None):
        """Ejecuta una consulta SELECT y retorna los resultados"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            print(f"Error en fetch query: {e}")
            return []
    
    def fetch_one(self, query, params=None):
        """Ejecuta una consulta SELECT y retorna un solo resultado"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            row = cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            print(f"Error en fetch one: {e}")
            return None

# Instancia global de la base de datos
db = Database()
