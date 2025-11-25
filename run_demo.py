"""
Modo DEMO - Ejecutar sin base de datos
Sistema funcional con datos en memoria
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
import hashlib
from functools import wraps

def simple_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_hash(hashed, password):
    return hashed == simple_hash(password)

app = Flask(__name__)
app.secret_key = 'demo_secret_key_2025'

# Datos en memoria (simulando base de datos)
usuarios_demo = {
    'admin@ecommerce.com': {
        'id_usuario': 1,
        'nombre': 'Admin Principal',
        'correo': 'admin@ecommerce.com',
        'password': simple_hash('admin123'),
        'rol': 'Administrador'
    },
    'empleado@ecommerce.com': {
        'id_usuario': 2,
        'nombre': 'Juan Empleado',
        'correo': 'empleado@ecommerce.com',
        'password': simple_hash('empleado123'),
        'rol': 'Empleado'
    },
    'cliente@email.com': {
        'id_usuario': 3,
        'nombre': 'María Cliente',
        'correo': 'cliente@email.com',
        'password': simple_hash('cliente123'),
        'rol': 'Cliente'
    }
}

productos_demo = [
    {'id_producto': 1, 'nombre': 'Laptop HP 15', 'descripcion': 'Laptop HP 15 pulgadas', 'precio': 12999.99, 'stock': 15, 'nivel_minimo': 5},
    {'id_producto': 2, 'nombre': 'Mouse Logitech', 'descripcion': 'Mouse inalámbrico', 'precio': 299.99, 'stock': 50, 'nivel_minimo': 10},
    {'id_producto': 3, 'nombre': 'Teclado Mecánico', 'descripcion': 'Teclado RGB gaming', 'precio': 1299.99, 'stock': 20, 'nivel_minimo': 5},
]

def login_required(roles=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Por favor inicia sesión', 'warning')
                return redirect(url_for('login'))
            if roles and session.get('rol') not in roles:
                flash('No tienes permisos', 'danger')
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/')
def index():
    return render_template('index.html', productos=productos_demo)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')
        
        usuario = usuarios_demo.get(correo)
        if usuario and check_hash(usuario['password'], password):
            session['user_id'] = usuario['id_usuario']
            session['nombre'] = usuario['nombre']
            session['rol'] = usuario['rol']
            flash(f'Bienvenido {usuario["nombre"]}', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas', 'danger')
    return render_template('login.html')

@app.route('/registro')
def registro():
    flash('Modo DEMO - Usa las credenciales predefinidas', 'info')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required()
def dashboard():
    rol = session.get('rol')
    if rol == 'Administrador':
        return render_template('dashboard_admin.html')
    elif rol == 'Empleado':
        return render_template('dashboard_empleado.html')
    else:
        return render_template('dashboard_cliente.html')

@app.route('/productos')
@login_required()
def productos_lista():
    return render_template('productos/lista.html', productos=productos_demo)

@app.route('/productos/<int:id>')
@login_required()
def producto_detalle(id):
    producto = next((p for p in productos_demo if p['id_producto'] == id), None)
    if producto:
        flash('Modo DEMO - Funcionalidad limitada', 'info')
        return render_template('index.html', productos=[producto])
    flash('Producto no encontrado', 'warning')
    return redirect(url_for('productos_lista'))

@app.route('/productos/crear')
@login_required(roles=['Administrador', 'Empleado'])
def producto_crear():
    flash('Modo DEMO - Esta función requiere base de datos', 'info')
    return redirect(url_for('productos_lista'))

@app.route('/pedidos')
@login_required()
def pedidos_lista():
    flash('Modo DEMO - No hay pedidos', 'info')
    return redirect(url_for('dashboard'))

@app.route('/proveedores')
@login_required(roles=['Administrador', 'Empleado'])
def proveedores_lista():
    flash('Modo DEMO - No hay proveedores', 'info')
    return redirect(url_for('dashboard'))

@app.route('/api/productos/stock-bajo')
@login_required(roles=['Administrador', 'Empleado'])
def productos_stock_bajo():
    productos_bajo = [p for p in productos_demo if p['stock'] < p['nivel_minimo']]
    return {'productos': productos_bajo}

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 MODO DEMO - Sistema de Comercio Electrónico")
    print("="*60)
    print("\n📝 Credenciales de acceso:")
    print("\n👑 Administrador:")
    print("   Email: admin@ecommerce.com")
    print("   Password: admin123")
    print("\n👤 Empleado:")
    print("   Email: empleado@ecommerce.com")
    print("   Password: empleado123")
    print("\n🛒 Cliente:")
    print("   Email: cliente@email.com")
    print("   Password: cliente123")
    print("\n" + "="*60)
    print("🌐 Abre tu navegador en: http://localhost:5001")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5001)
