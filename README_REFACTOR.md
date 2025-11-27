# Refactorización: Sistema de 3 Roles de Usuario

Este documento describe la refactorización del sistema de e-commerce para usar únicamente 3 roles de usuario: **Administrador**, **Trabajador** y **Proveedor**.

## 🎯 Cambios Principales

### Eliminado
- ❌ Rol "Cliente" y tabla CLIENTE
- ❌ Rol "Empleado" (renombrado a "Trabajador")
- ❌ Rutas de carrito de compras y checkout
- ❌ Registro público de usuarios
- ❌ Plantillas relacionadas con clientes

### Agregado
- ✅ Rol "Trabajador" con funcionalidad de ventas directas
- ✅ Rol "Proveedor" como usuario del sistema
- ✅ Tabla PROVEEDOR_USUARIO para vincular usuarios proveedores con empresas
- ✅ Campo `procesado_por` en tabla PEDIDO
- ✅ Botones de inicio de sesión rápido en login
- ✅ Interfaz de ventas para trabajadores
- ✅ Dashboards específicos para cada rol

## 👥 Roles y Funcionalidades

### 👨‍💼 Administrador
- Ver y gestionar inventario completo
- Agregar, editar y eliminar productos
- Ver todos los pedidos del sistema
- Gestionar proveedores
- Control total del sistema

### 👷 Trabajador
- Procesar ventas directas
- Reducir inventario automáticamente al vender
- Ver historial de sus propias ventas
- Consultar productos disponibles

### 🚚 Proveedor
- Consultar inventario (solo lectura)
- Ver productos con stock bajo
- Registrar abastecimientos de productos
- Ver historial de abastecimientos

## 🚀 Aplicar la Refactorización

### Opción 1: Script Automático (Recomendado)

```bash
./aplicar_refactor.sh
```

Este script:
1. Elimina la base de datos anterior
2. Crea una nueva base de datos
3. Aplica el nuevo schema (`schema_refactor.sql`)
4. Inserta los datos de prueba (`seed_refactor.py`)

### Opción 2: Manual

```bash
# 1. Eliminar base de datos anterior
mysql -u root -p -e "DROP DATABASE IF EXISTS ecommerce_db;"

# 2. Crear nueva base de datos
mysql -u root -p -e "CREATE DATABASE ecommerce_db;"

# 3. Aplicar nuevo schema
mysql -u root -p ecommerce_db < schema_refactor.sql

# 4. Insertar datos de prueba
python3 seed_refactor.py
```

## 🔑 Usuarios de Prueba

Después de aplicar la refactorización, podrás iniciar sesión con:

### Administrador
- **Email:** admin@ecommerce.com
- **Password:** admin123

### Trabajador
- **Email:** trabajador@ecommerce.com
- **Password:** trabajador123

### Proveedor
- **Email:** proveedor@ecommerce.com
- **Password:** proveedor123

## 🎨 Interfaz de Usuario

### Pantalla de Login
La pantalla de login ahora incluye **3 botones de acceso rápido** para iniciar sesión directamente con cada tipo de usuario, sin necesidad de recordar las credenciales.

### Dashboards
- **dashboard_admin.html**: Panel completo con todas las funcionalidades
- **dashboard_trabajador.html**: Enfocado en ventas y consulta de inventario
- **dashboard_proveedor.html**: Consulta de inventario y abastecimientos

### Ventas
Nueva interfaz en `/ventas` para que trabajadores procesen ventas:
- Selección múltiple de productos
- Cálculo automático de total
- Reducción automática de inventario
- Registro del trabajador que procesó la venta

## 📁 Archivos Nuevos/Modificados

### Base de Datos
- `schema_refactor.sql` - Nuevo schema con 3 roles
- `seed_refactor.py` - Datos de prueba para 3 usuarios
- `aplicar_refactor.sh` - Script de aplicación automática

### Backend
- `app.py` - Rutas actualizadas, eliminadas rutas de cliente, agregadas rutas de venta
- `models/usuario.py` - Eliminada lógica de tabla CLIENTE
- `models/pedido.py` - Actualizado para usar `id_usuario` y `procesado_por`

### Frontend
- `templates/login.html` - Botones de acceso rápido
- `templates/dashboard_trabajador.html` - Dashboard de trabajador (nuevo)
- `templates/dashboard_proveedor.html` - Dashboard de proveedor (nuevo)
- `templates/ventas/crear.html` - Interfaz de ventas (nuevo)
- `templates/dashboard_empleado.html` - Ya no se usa
- `templates/dashboard_cliente.html` - Eliminado
- `templates/carrito/` - Directorio eliminado
- `templates/registro.html` - Ya no se usa

## 🔄 Diferencias en la Base de Datos

### Tabla USUARIO
```sql
-- Antes
rol ENUM('Administrador', 'Empleado', 'Cliente')

-- Después
rol ENUM('Administrador', 'Trabajador', 'Proveedor')
```

### Tabla PEDIDO
```sql
-- Antes
id_cliente INT NOT NULL

-- Después
id_usuario INT NOT NULL
procesado_por INT NULL  -- ID del trabajador
```

### Nueva Tabla
```sql
-- PROVEEDOR_USUARIO: vincula usuarios proveedores con empresas
CREATE TABLE PROVEEDOR_USUARIO (
  id_proveedor INT NOT NULL,
  id_usuario INT NOT NULL,
  PRIMARY KEY (id_proveedor, id_usuario)
)
```

### Tabla Eliminada
- ❌ `CLIENTE` (ya no existe)

## ⚠️ Notas Importantes

1. **Backup**: Este proceso elimina la base de datos anterior. Si tienes datos importantes, haz un backup primero.

2. **Pedidos**: En el nuevo sistema, los pedidos se relacionan directamente con usuarios (trabajadores), no con clientes externos.

3. **Proveedores**: Ahora son usuarios del sistema con acceso de solo lectura al inventario y capacidad de registrar abastecimientos.

4. **Sin Registro Público**: Ya no existe registro público. Solo el administrador puede crear nuevos usuarios.

## 🐛 Solución de Problemas

### Error: "No se encontró el archivo .env"
Asegúrate de tener un archivo `.env` con las credenciales de la base de datos:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_password
DB_NAME=ecommerce_db
```

### Error al conectar a MySQL
Verifica que el servidor MySQL esté corriendo:
```bash
mysql.server status
# o
sudo systemctl status mysql
```

### Error en seed_refactor.py
Asegúrate de tener instaladas las dependencias:
```bash
pip install -r requirements.txt
```

## 📞 Soporte

Si tienes problemas con la refactorización, revisa:
1. Los logs de la aplicación
2. Los permisos de usuario en MySQL
3. Que todas las dependencias estén instaladas
4. Que el schema se haya aplicado correctamente

---

**Versión:** 2.0 (Sistema Refactorizado)  
**Fecha:** Noviembre 2024
