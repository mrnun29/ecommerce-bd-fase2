# Implementaciones Pendientes

## ✅ Completado
1. ✅ Botones de acceso rápido removidos del login
2. ✅ Sistema de creación de usuarios por admin (ruta `/usuarios/crear`)

## 🔄 Pendientes de Implementar

### 3. Historial de Cambios en Inventario

**Crear tabla en MySQL:**
```sql
CREATE TABLE IF NOT EXISTS `HISTORIAL_INVENTARIO` (
  `id_historial` INT NOT NULL AUTO_INCREMENT,
  `id_producto` INT NOT NULL,
  `id_usuario` INT NOT NULL,
  `stock_anterior` INT NOT NULL,
  `stock_nuevo` INT NOT NULL,
  `motivo` VARCHAR(200),
  `fecha` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_historial`),
  INDEX `fk_HISTORIAL_PRODUCTO_idx` (`id_producto` ASC),
  INDEX `fk_HISTORIAL_USUARIO_idx` (`id_usuario` ASC),
  CONSTRAINT `fk_HISTORIAL_PRODUCTO`
    FOREIGN KEY (`id_producto`)
    REFERENCES `PRODUCTO` (`id_producto`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_HISTORIAL_USUARIO`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `USUARIO` (`id_usuario`)
    ON DELETE CASCADE
) ENGINE = InnoDB;
```

**Modificar `models/producto.py` - agregar al método `actualizar`:**
```python
# Antes de actualizar, obtener stock actual
producto_actual = Producto.obtener_por_id(id_producto)
stock_anterior = producto_actual['stock']

# Después de UPDATE PRODUCTO, registrar en historial si el stock cambió
if datos['stock'] != stock_anterior:
    query_historial = """
        INSERT INTO HISTORIAL_INVENTARIO 
        (id_producto, id_usuario, stock_anterior, stock_nuevo, motivo)
        VALUES (%s, %s, %s, %s, %s)
    """
    # Nota: necesitas pasar id_usuario desde la ruta
    db.execute_query(query_historial, (
        id_producto,
        session['user_id'],  # Esto debe venir como parámetro
        stock_anterior,
        datos['stock'],
        'Edición manual de inventario'
    ))
```

### 4. Validación de Tarjeta en Ventas

**Modificar `templates/ventas/crear.html` - agregar JavaScript:**
```javascript
// Formateo automático de número de tarjeta (espacios cada 4 dígitos)
document.getElementById('num_tarjeta').addEventListener('input', function(e) {
    let value = e.target.value.replace(/\s/g, '');
    let formatted = value.match(/.{1,4}/g)?.join(' ') || value;
    e.target.value = formatted;
});

// Formateo automático de fecha MM/AA
document.getElementById('vencimiento').addEventListener('input', function(e) {
    let value = e.target.value.replace(/\//g, '');
    if (value.length >= 2) {
        e.target.value = value.slice(0,2) + '/' + value.slice(2,4);
    } else {
        e.target.value = value;
    }
});

// Validación antes de submit
document.getElementById('form-pago').addEventListener('submit', function(e) {
    const tipoPago = document.getElementById('tipoPago').value;
    
    if (tipoPago === 'Tarjeta') {
        const numTarjeta = document.getElementById('num_tarjeta').value.replace(/\s/g, '');
        const vencimiento = document.getElementById('vencimiento').value;
        const cvv = document.getElementById('cvv').value;
        
        if (numTarjeta.length !== 16) {
            alert('El número de tarjeta debe tener 16 dígitos');
            e.preventDefault();
            return false;
        }
        
        if (!/^\d{2}\/\d{2}$/.test(vencimiento)) {
            alert('Formato de fecha inválido (MM/AA)');
            e.preventDefault();
            return false;
        }
        
        if (cvv.length !== 3 && cvv.length !== 4) {
            alert('CVV inválido (3 o 4 dígitos)');
            e.preventDefault();
            return false;
        }
    }
});
```

### 5. Historial de Reabastecimiento para Proveedor

**Agregar ruta en `app.py`:**
```python
@app.route('/proveedor/historial')
@login_required(roles=['Proveedor'])
def proveedor_historial():
    """Historial de reabastecimientos del proveedor"""
    # Obtener id_proveedor del usuario actual
    query_proveedor = """
        SELECT id_proveedor FROM PROVEEDOR_USUARIO
        WHERE id_usuario = %s
    """
    result = db.fetch_one(query_proveedor, (session['user_id'],))
    
    if not result:
        flash('No estás vinculado a ningún proveedor', 'warning')
        return redirect(url_for('dashboard'))
    
    id_proveedor = result['id_proveedor']
    
    # Obtener historial
    historial = Proveedor.obtener_productos_abastecidos(id_proveedor)
    
    return render_template('proveedor/historial.html', historial=historial)
```

**Crear `templates/proveedor/historial.html`:**
```html
{% extends "base.html" %}

{% block title %}Historial de Reabastecimiento{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-12">
        <h2><i class="bi bi-clock-history"></i> Historial de Reabastecimientos</h2>
        <p class="text-muted">Registro de todos los productos que has reabastecido</p>
    </div>
</div>

<div class="row">
    <div class="col-12">
        {% if historial %}
        <div class="card shadow-sm">
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th>Fecha</th>
                                <th>Producto</th>
                                <th>Cantidad</th>
                                <th>Stock Actual</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for item in historial %}
                            <tr>
                                <td>{{ item.fecha_abastecimiento.strftime('%d/%m/%Y %H:%M') }}</td>
                                <td><strong>{{ item.nombre }}</strong></td>
                                <td><span class="badge bg-success">+{{ item.cantidad }}</span></td>
                                <td>{{ item.stock }} unidades</td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        {% else %}
        <div class="alert alert-info">
            <i class="bi bi-info-circle"></i> No has realizado reabastecimientos aún.
            <a href="{{ url_for('proveedores_stock_bajo') }}" class="alert-link">Ver productos con stock bajo</a>
        </div>
        {% endif %}
    </div>
</div>

<div class="row mt-4">
    <div class="col-12">
        <a href="{{ url_for('dashboard') }}" class="btn btn-secondary">
            <i class="bi bi-arrow-left"></i> Volver al Dashboard
        </a>
    </div>
</div>
{% endblock %}
```

### 6. Template de Lista de Usuarios

**Crear `templates/usuarios/lista.html`:**
```html
{% extends "base.html" %}

{% block title %}Gestión de Usuarios{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-12">
        <div class="d-flex justify-content-between align-items-center">
            <div>
                <h2><i class="bi bi-people"></i> Gestión de Usuarios</h2>
                <p class="text-muted">Administración de cuentas del sistema</p>
            </div>
            <a href="{{ url_for('usuario_crear') }}" class="btn btn-primary">
                <i class="bi bi-person-plus"></i> Nuevo Usuario
            </a>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <div class="card shadow-sm">
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Nombre</th>
                                <th>Correo</th>
                                <th>Rol</th>
                                <th>Dirección</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for usuario in usuarios %}
                            <tr>
                                <td>{{ usuario.id_usuario }}</td>
                                <td><strong>{{ usuario.nombre }}</strong></td>
                                <td>{{ usuario.correo }}</td>
                                <td>
                                    <span class="badge 
                                        {% if usuario.rol == 'Administrador' %}bg-danger
                                        {% elif usuario.rol == 'Trabajador' %}bg-success
                                        {% else %}bg-info{% endif %}">
                                        {{ usuario.rol }}
                                    </span>
                                </td>
                                <td>{{ usuario.ciudad }}</td>
                                <td>
                                    <button class="btn btn-sm btn-outline-primary" disabled>
                                        <i class="bi bi-pencil"></i>
                                    </button>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-12">
        <a href="{{ url_for('dashboard') }}" class="btn btn-secondary">
            <i class="bi bi-arrow-left"></i> Volver al Dashboard
        </a>
    </div>
</div>
{% endblock %}
```

### 7. Agregar enlaces al Dashboard Admin

**Modificar `templates/dashboard_admin.html` - agregar card:**
```html
<div class="col-md-4 mb-3">
    <div class="card shadow-sm h-100">
        <div class="card-body">
            <h5 class="card-title">
                <i class="bi bi-people text-primary"></i> Gestión de Usuarios
            </h5>
            <p class="card-text">Crear y administrar cuentas de trabajadores y proveedores.</p>
            <a href="{{ url_for('usuarios_lista') }}" class="btn btn-primary">
                <i class="bi bi-people"></i> Administrar Usuarios
            </a>
        </div>
    </div>
</div>
```

## Comandos para Aplicar

```bash
# 1. Agregar tabla de historial
mysql -u root -pRoot@Pass123 ecommerce_db < historial_inventario.sql

# 2. Crear directorio para proveedor
mkdir -p templates/proveedor

# 3. Reiniciar Flask
kill $(cat flask.pid) 2>/dev/null
cd /Users/diegomita/ecommerce_db && source .venv/bin/activate && export $(cat .env | xargs) && nohup python app.py > flask.log 2>&1 & echo $! > flask.pid
```

## Notas Importantes

- Las validaciones de tarjeta son solo del lado del cliente (fake)
- El historial de inventario requiere modificar las rutas para pasar user_id
- Los logs de error se pueden implementar usando el sistema de logging de Python
- La capacidad de archivar pedidos requiere agregar un campo `archivado` a la tabla PEDIDO
