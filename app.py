"""
Sistema de Comercio Electrónico con Gestión de Inventarios
Aplicación Principal - Flask
Fase 2: Implementación
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from config.database import db
from models.usuario import Usuario
from models.producto import Producto
from models.pedido import Pedido, Pago
from models.proveedor import Proveedor
import os
import hashlib

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'clave_secreta_desarrollo_2025')

# Filtros personalizados para Jinja2
@app.template_filter('obtener_productos_pedido')
def obtener_productos_pedido_filter(id_pedido):
    return Pedido.obtener_productos_pedido(id_pedido)

@app.template_filter('obtener_pago_pedido')
def obtener_pago_pedido_filter(id_pedido):
    return Pago.obtener_por_pedido(id_pedido)

# Conectar a la base de datos al iniciar
@app.before_request
def before_request():
    if not db.connection or not db.connection.is_connected():
        db.connect()

# Decorador para proteger rutas según rol
def login_required(roles=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Por favor inicia sesión', 'warning')
                return redirect(url_for('login'))
            
            if roles and session.get('rol') not in roles:
                flash('No tienes permisos para acceder a esta página', 'danger')
                return redirect(url_for('index'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# ============= RUTAS PÚBLICAS =============

@app.route('/')
def index():
    """Página principal"""
    productos = Producto.obtener_todos()
    return render_template('index.html', productos=productos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Inicio de sesión"""
    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')
        
        usuario = Usuario.buscar_por_correo(correo)
        
        # Hash MD5 de la contraseña
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        if usuario and usuario['password'] == password_hash:
            session['user_id'] = usuario['id_usuario']
            session['nombre'] = usuario['nombre']
            session['rol'] = usuario['rol']
            flash(f'Bienvenido {usuario["nombre"]}', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """Cerrar sesión"""
    session.clear()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('index'))

# ============= DASHBOARD =============

@app.route('/dashboard')
@login_required()
def dashboard():
    """Panel principal según rol"""
    rol = session.get('rol')
    
    if rol == 'Administrador':
        return render_template('dashboard_admin.html')
    elif rol == 'Trabajador':
        return render_template('dashboard_trabajador.html')
    else:  # Proveedor
        return render_template('dashboard_proveedor.html')

# ============= PRODUCTOS =============

@app.route('/productos')
@login_required()
def productos_lista():
    """Lista de productos"""
    productos = Producto.obtener_todos()
    return render_template('productos/lista.html', productos=productos)

@app.route('/productos/crear', methods=['GET', 'POST'])
@login_required(roles=['Administrador'])
def producto_crear():
    """Crear nuevo producto"""
    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'descripcion': request.form.get('descripcion'),
            'precio': float(request.form.get('precio')),
            'stock': int(request.form.get('stock')),
            'nivel_minimo': int(request.form.get('nivel_minimo', 10)),
            'imagen': request.form.get('imagen')
        }
        
        if Producto.crear(datos):
            flash('Producto creado exitosamente', 'success')
            return redirect(url_for('productos_lista'))
        else:
            flash('Error al crear producto', 'danger')
    
    return render_template('productos/crear.html')

@app.route('/productos/<int:id>')
@login_required()
def producto_detalle(id):
    """Ver detalle de producto"""
    producto = Producto.obtener_por_id(id)
    if producto:
        return render_template('productos/detalle.html', producto=producto)
    else:
        flash('Producto no encontrado', 'warning')
        return redirect(url_for('productos_lista'))

@app.route('/productos/<int:id>/editar', methods=['GET', 'POST'])
@login_required(roles=['Administrador'])
def producto_editar(id):
    """Editar producto"""
    producto = Producto.obtener_por_id(id)
    
    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'descripcion': request.form.get('descripcion'),
            'precio': float(request.form.get('precio')),
            'stock': int(request.form.get('stock')),
            'nivel_minimo': int(request.form.get('nivel_minimo')),
            'imagen': request.form.get('imagen')
        }
        
        if Producto.actualizar(id, datos):
            flash('Producto actualizado', 'success')
            return redirect(url_for('producto_detalle', id=id))
        else:
            flash('Error al actualizar', 'danger')
    
    return render_template('productos/editar.html', producto=producto)

@app.route('/productos/<int:id>/eliminar', methods=['POST'])
@login_required(roles=['Administrador'])
def producto_eliminar(id):
    """Eliminar producto"""
    if Producto.eliminar(id):
        flash('Producto eliminado', 'success')
    else:
        flash('Error al eliminar producto', 'danger')
    return redirect(url_for('productos_lista'))

# ============= PEDIDOS =============

@app.route('/pedidos')
@login_required()
def pedidos_lista():
    """Lista de pedidos"""
    rol = session.get('rol')
    if rol == 'Administrador':
        pedidos = Pedido.obtener_todos()
    elif rol == 'Trabajador':
        pedidos = Pedido.obtener_por_trabajador(session.get('user_id'))
    else:  # Proveedor - no tiene acceso a pedidos
        flash('No tienes permisos para ver pedidos', 'danger')
        return redirect(url_for('dashboard'))
    return render_template('pedidos/lista.html', pedidos=pedidos)

@app.route('/pedidos/<int:id>')
@login_required()
def pedido_detalle(id):
    """Ver detalle de pedido"""
    pedido = Pedido.obtener_por_id(id)
    if pedido:
        return render_template('pedidos/detalle.html', pedido=pedido)
    else:
        flash('Pedido no encontrado', 'warning')
        return redirect(url_for('pedidos_lista'))

@app.route('/pedidos/<int:id_pedido>/actualizar', methods=['POST'])
@login_required(roles=['Administrador', 'Trabajador'])
def actualizar_estado_pedido(id_pedido):
    """Actualizar estado de un pedido"""
    nuevo_estado = request.form.get('nuevo_estado')
    if Pedido.actualizar_estado(id_pedido, nuevo_estado):
        flash(f'Estado actualizado a {nuevo_estado}', 'success')
    else:
        flash('Error al actualizar estado', 'danger')
    return redirect(url_for('pedido_detalle', id=id_pedido))

# ============= PROVEEDORES =============

@app.route('/proveedores')
@login_required(roles=['Administrador'])
def proveedores_lista():
    """Lista de proveedores con sus usuarios"""
    proveedores = Proveedor.obtener_proveedores_con_usuarios()
    return render_template('proveedores/lista.html', proveedores=proveedores)

@app.route('/proveedores/usuarios')
@login_required(roles=['Administrador'])
def proveedores_usuarios():
    """Vista de proveedores y trabajadores"""
    # Obtener todos los trabajadores
    from models.usuario import Usuario
    trabajadores = Usuario.obtener_por_rol('Trabajador')
    
    # Obtener proveedores con sus usuarios
    proveedores = Proveedor.obtener_proveedores_con_usuarios()
    
    return render_template('proveedores/usuarios.html', proveedores=proveedores, trabajadores=trabajadores)

@app.route('/proveedores/crear', methods=['GET', 'POST'])
@login_required(roles=['Administrador'])
def proveedor_crear():
    """Crear nuevo proveedor"""
    if request.method == 'POST':
        datos = {
            'contacto': request.form.get('contacto'),
            'empresa': request.form.get('empresa'),
            'calle': request.form.get('calle'),
            'numero': request.form.get('numero'),
            'ciudad': request.form.get('ciudad'),
            'codigo_postal': request.form.get('codigo_postal')
        }
        
        if Proveedor.crear(datos):
            flash('Proveedor creado exitosamente', 'success')
            return redirect(url_for('proveedores_lista'))
        else:
            flash('Error al crear proveedor', 'danger')
    
    return render_template('proveedores/crear.html')

@app.route('/proveedores/stock-bajo')
@login_required(roles=['Administrador', 'Proveedor'])
def proveedores_stock_bajo():
    """Ver productos con stock bajo para reabastecer"""
    productos = Producto.obtener_stock_bajo()
    proveedores = Proveedor.obtener_todos()
    return render_template('proveedores/stock_bajo.html', productos=productos, proveedores=proveedores)

@app.route('/proveedores/reabastecer', methods=['POST'])
@login_required(roles=['Administrador', 'Proveedor'])
def reabastecer_producto():
    """Reabastecer un producto"""
    id_producto = int(request.form.get('id_producto'))
    id_proveedor = int(request.form.get('id_proveedor'))
    cantidad = int(request.form.get('cantidad'))
    
    # Registrar abastecimiento
    if Proveedor.abastecer_producto(id_proveedor, id_producto, cantidad):
        flash(f'Producto reabastecido con {cantidad} unidades', 'success')
    else:
        flash('Error al reabastecer producto', 'danger')
    
    return redirect(url_for('proveedores_stock_bajo'))


# ============= VENTAS (TRABAJADORES) =============

@app.route('/ventas')
@login_required(roles=['Trabajador'])
def ventas():
    """Interfaz de ventas para trabajadores"""
    productos = Producto.obtener_todos()
    return render_template('ventas/crear.html', productos=productos)

@app.route('/ventas/procesar', methods=['POST'])
@login_required(roles=['Trabajador'])
def procesar_venta():
    """Procesar una venta directa"""
    try:
        # Obtener productos del formulario
        productos_ids = request.form.getlist('productos[]')
        cantidades = request.form.getlist('cantidades[]')
        
        if not productos_ids:
            flash('Debes seleccionar al menos un producto', 'warning')
            return redirect(url_for('ventas'))
        
        # Preparar lista de productos
        productos = []
        for i, id_prod in enumerate(productos_ids):
            if id_prod and cantidades[i]:
                producto = Producto.obtener_por_id(int(id_prod))
                if producto:
                    productos.append({
                        'id_producto': producto['id_producto'],
                        'cantidad': int(cantidades[i]),
                        'precio_unitario': producto['precio']
                    })
        
        # Crear pedido (sin cliente específico, procesado por trabajador)
        id_pedido = Pedido.crear(
            id_usuario=session['user_id'],  # El trabajador mismo
            productos=productos,
            procesado_por=session['user_id']
        )
        
        if id_pedido:
            # Procesar pago
            tipo_pago = request.form.get('tipo_pago', 'Efectivo')
            total = sum(p['cantidad'] * p['precio_unitario'] for p in productos)
            
            detalles_pago = {}
            if tipo_pago == 'Efectivo':
                from datetime import datetime, timedelta
                detalles_pago = {
                    'folio': id_pedido,  # Usar el ID del pedido como folio
                    'fecha_limite': datetime.now() + timedelta(days=1)
                }
            elif tipo_pago == 'Tarjeta':
                detalles_pago = {
                    'num_tarjeta': '4111111111111111',  # Número fake
                    'banco': 'DEMO',
                    'vencimiento': '2025-12-31',
                    'cuenta': '1234'
                }
            elif tipo_pago == 'Transferencia':
                detalles_pago = {
                    'referencia': f'REF{id_pedido}'
                }
            
            id_pago = Pago.crear(id_pedido, total, tipo_pago, detalles_pago)
            
            if id_pago:
                flash(f'Venta procesada exitosamente. Pedido #{id_pedido}', 'success')
                return redirect(url_for('pedido_detalle', id=id_pedido))
            else:
                flash('Error al procesar el pago', 'danger')
        else:
            flash('Error al procesar la venta', 'danger')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
    
    return redirect(url_for('ventas'))

# ============= INVENTARIO (ADMINISTRADOR) =============

@app.route('/inventario')
@login_required(roles=['Administrador', 'Proveedor'])
def inventario():
    """Ver y gestionar inventario"""
    productos = Producto.obtener_todos()
    productos_bajo_stock = Producto.obtener_stock_bajo()
    return render_template('inventario/lista.html', productos=productos, productos_bajo_stock=productos_bajo_stock)

@app.route('/inventario/<int:id_producto>/editar', methods=['GET', 'POST'])
@login_required(roles=['Administrador'])
def inventario_editar(id_producto):
    """Editar inventario de un producto"""
    producto = Producto.obtener_por_id(id_producto)
    
    if request.method == 'POST':
        nuevo_stock = int(request.form.get('stock'))
        nivel_minimo = int(request.form.get('nivel_minimo'))
        
        datos = {
            'nombre': producto['nombre'],
            'descripcion': producto['descripcion'],
            'precio': producto['precio'],
            'stock': nuevo_stock,
            'nivel_minimo': nivel_minimo,
            'imagen': producto['imagen']
        }
        
        if Producto.actualizar(id_producto, datos):
            flash('Inventario actualizado', 'success')
            return redirect(url_for('inventario'))
        else:
            flash('Error al actualizar inventario', 'danger')
    
    return render_template('inventario/editar.html', producto=producto)

# ============= API/BÚSQUEDAS =============

@app.route('/api/productos/buscar')
@login_required()
def buscar_productos():
    """Buscar productos por nombre"""
    termino = request.args.get('q', '')
    productos = Producto.buscar(termino)
    return {'productos': productos}

@app.route('/api/productos/stock-bajo')
@login_required(roles=['Administrador', 'Proveedor'])
def productos_stock_bajo():
    """Obtener productos con stock bajo"""
    productos = Producto.obtener_stock_bajo()
    return {'productos': productos}

# ============= MANEJO DE ERRORES =============

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
