"""
Sistema de Comercio Electrónico con Gestión de Inventarios
Aplicación Principal - Flask
Fase 2: Implementación
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from config.database import db
from models.usuario import Usuario
from models.producto import Producto
from models.pedido import Pedido
from models.proveedor import Proveedor
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'clave_secreta_desarrollo_2025')

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
        
        if usuario and check_password_hash(usuario['password'], password):
            session['user_id'] = usuario['id_usuario']
            session['nombre'] = usuario['nombre']
            session['rol'] = usuario['rol']
            flash(f'Bienvenido {usuario["nombre"]}', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas', 'danger')
    
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    """Registro de nuevo usuario"""
    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'correo': request.form.get('correo'),
            'password': generate_password_hash(request.form.get('password')),
            'rol': 'Cliente',
            'calle': request.form.get('calle'),
            'numero': request.form.get('numero'),
            'ciudad': request.form.get('ciudad'),
            'codigo_postal': request.form.get('codigo_postal')
        }
        
        if Usuario.crear(datos):
            flash('Usuario registrado exitosamente', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error al registrar usuario', 'danger')
    
    return render_template('registro.html')

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
    elif rol == 'Empleado':
        return render_template('dashboard_empleado.html')
    else:
        return render_template('dashboard_cliente.html')

# ============= PRODUCTOS =============

@app.route('/productos')
@login_required()
def productos_lista():
    """Lista de productos"""
    productos = Producto.obtener_todos()
    return render_template('productos/lista.html', productos=productos)

@app.route('/productos/crear', methods=['GET', 'POST'])
@login_required(roles=['Administrador', 'Empleado'])
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
@login_required(roles=['Administrador', 'Empleado'])
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
    if session.get('rol') == 'Cliente':
        pedidos = Pedido.obtener_por_cliente(session.get('user_id'))
    else:
        pedidos = Pedido.obtener_todos()
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

# ============= PROVEEDORES =============

@app.route('/proveedores')
@login_required(roles=['Administrador', 'Empleado'])
def proveedores_lista():
    """Lista de proveedores"""
    proveedores = Proveedor.obtener_todos()
    return render_template('proveedores/lista.html', proveedores=proveedores)

@app.route('/proveedores/crear', methods=['GET', 'POST'])
@login_required(roles=['Administrador', 'Empleado'])
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

# ============= API/BÚSQUEDAS =============

@app.route('/api/productos/buscar')
@login_required()
def buscar_productos():
    """Buscar productos por nombre"""
    termino = request.args.get('q', '')
    productos = Producto.buscar(termino)
    return {'productos': productos}

@app.route('/api/productos/stock-bajo')
@login_required(roles=['Administrador', 'Empleado'])
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
