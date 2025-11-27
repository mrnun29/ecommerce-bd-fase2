"""
Modelo Carrito
Gestiona el carrito de compras temporal en la sesión
"""
from config.database import db
from models.producto import Producto

class Carrito:
    
    @staticmethod
    def agregar_item(carrito_session, id_producto, cantidad=1):
        """
        Agregar producto al carrito en sesión
        carrito_session: dict con estructura {id_producto: {'cantidad': X, 'producto': {...}}}
        """
        producto = Producto.obtener_por_id(id_producto)
        
        if not producto:
            return False, "Producto no encontrado"
        
        if producto['stock'] < cantidad:
            return False, f"Stock insuficiente. Disponible: {producto['stock']}"
        
        if str(id_producto) in carrito_session:
            nueva_cantidad = carrito_session[str(id_producto)]['cantidad'] + cantidad
            if producto['stock'] < nueva_cantidad:
                return False, f"Stock insuficiente. Disponible: {producto['stock']}"
            carrito_session[str(id_producto)]['cantidad'] = nueva_cantidad
        else:
            carrito_session[str(id_producto)] = {
                'cantidad': cantidad,
                'producto': {
                    'id_producto': producto['id_producto'],
                    'nombre': producto['nombre'],
                    'precio': float(producto['precio']),
                    'imagen': producto['imagen']
                }
            }
        
        return True, "Producto agregado al carrito"
    
    @staticmethod
    def actualizar_cantidad(carrito_session, id_producto, cantidad):
        """Actualizar cantidad de un producto en el carrito"""
        if str(id_producto) not in carrito_session:
            return False, "Producto no encontrado en el carrito"
        
        producto = Producto.obtener_por_id(id_producto)
        if not producto:
            return False, "Producto no encontrado"
        
        if cantidad <= 0:
            del carrito_session[str(id_producto)]
            return True, "Producto eliminado del carrito"
        
        if producto['stock'] < cantidad:
            return False, f"Stock insuficiente. Disponible: {producto['stock']}"
        
        carrito_session[str(id_producto)]['cantidad'] = cantidad
        return True, "Cantidad actualizada"
    
    @staticmethod
    def remover_item(carrito_session, id_producto):
        """Remover producto del carrito"""
        if str(id_producto) in carrito_session:
            del carrito_session[str(id_producto)]
            return True
        return False
    
    @staticmethod
    def obtener_total(carrito_session):
        """Calcular el total del carrito"""
        total = 0
        for item in carrito_session.values():
            total += item['cantidad'] * item['producto']['precio']
        return total
    
    @staticmethod
    def obtener_cantidad_items(carrito_session):
        """Obtener cantidad total de items en el carrito"""
        return sum(item['cantidad'] for item in carrito_session.values())
    
    @staticmethod
    def limpiar(carrito_session):
        """Vaciar el carrito"""
        carrito_session.clear()
        return True
