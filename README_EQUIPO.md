# 🛒 Sistema de Comercio Electrónico - Fase 2

**Proyecto de Bases de Datos**  
Universidad Anáhuac Querétaro

## 👥 Equipo de Desarrollo
- Alberto Romero Mañón (00439959)
- Diego Nuñez Chavez (00516279)
- Emilio Antonio Tolosa Soto (00520630)
- Diego Vega Cabrera (00509910)

**Profesor:** Jonathan Omar Rendón Zamora

---

## 🚀 Inicio Rápido para el Equipo

### Opción 1: Con Docker (RECOMENDADO) ⭐

**Requisitos:**
- Docker Desktop instalado

**Pasos:**

```bash
# 1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd ecommerce_db

# 2. Levantar todo con Docker
docker-compose up --build

# 3. En otra terminal, insertar datos de prueba
docker-compose exec web python docker_seed.py

# 4. Abrir navegador
# http://localhost:5001
```

**¡Listo!** No necesitas instalar MySQL ni Python localmente.

---

### Opción 2: Sin Docker (Instalación Manual)

**Requisitos:**
- Python 3.8+
- MySQL 8.0+

**Pasos:**

```bash
# 1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd ecommerce_db

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar base de datos
cp .env.example .env
# Editar .env con tus credenciales de MySQL

# 5. Crear base de datos
mysql -u root -p < schema.sql

# 6. Insertar datos de prueba
python seed_data.py

# 7. Ejecutar aplicación
python app.py

# 8. Abrir navegador
# http://localhost:5001
```

---

## 🔑 Credenciales de Acceso

Una vez que hayas insertado los datos de prueba:

| Rol | Email | Contraseña |
|-----|-------|------------|
| 👑 **Administrador** | admin@ecommerce.com | admin123 |
| 👤 **Empleado** | empleado@ecommerce.com | empleado123 |
| 🛒 **Cliente** | cliente@email.com | cliente123 |

---

## 📁 Estructura del Proyecto

```
ecommerce_db/
├── app.py                      # Aplicación Flask principal
├── run_demo.py                 # Versión demo sin BD
├── docker-compose.yml          # Configuración Docker
├── Dockerfile                  # Imagen Docker
├── requirements.txt            # Dependencias Python
├── schema.sql                  # Script de creación de BD
├── seed_data.py               # Datos de prueba
├── docker_seed.py             # Datos de prueba para Docker
├── config/
│   ├── database.py            # Conexión MySQL
│   └── database_sqlite.py     # Conexión SQLite (alternativa)
├── models/
│   ├── usuario.py             # Modelo Usuario
│   ├── producto.py            # Modelo Producto
│   ├── pedido.py              # Modelo Pedido
│   └── proveedor.py           # Modelo Proveedor
└── templates/
    ├── base.html              # Plantilla base
    ├── index.html             # Página principal
    ├── login.html             # Login
    ├── registro.html          # Registro
    ├── dashboard_*.html       # Dashboards por rol
    └── productos/             # Vistas de productos
        └── pedidos/           # Vistas de pedidos
            └── proveedores/   # Vistas de proveedores
```

---

## 🎯 Funcionalidades Implementadas

### ✅ Fase 2 - Completada

- [x] **Sistema de Autenticación**
  - Login/Registro
  - 3 roles: Administrador, Empleado, Cliente
  - Control de acceso basado en permisos

- [x] **Gestión de Productos (CRUD)**
  - Crear, leer, actualizar, eliminar productos
  - Control de stock automático
  - Alertas de stock bajo

- [x] **Gestión de Pedidos**
  - Crear pedidos con múltiples productos
  - Estados: Pendiente, Procesando, Enviado, Entregado, Cancelado
  - Descuento automático de inventario

- [x] **Sistema de Pagos**
  - Tarjeta, Transferencia, Efectivo
  - Registro de pagos por pedido

- [x] **Gestión de Proveedores**
  - CRUD de proveedores
  - Relación con productos
  - Registro de abastecimientos

- [x] **Reportes y Consultas**
  - Productos más vendidos
  - Ventas por periodo
  - Stock bajo
  - Gasto promedio por cliente

- [x] **Validaciones**
  - Front-end: campos obligatorios, formatos
  - Back-end: integridad referencial, stock disponible

---

## 🗄️ Base de Datos

### Tablas Principales

- `USUARIO` - Usuarios del sistema
- `CLIENTE` - Información de clientes
- `PROVEEDOR` - Proveedores
- `PRODUCTO` - Catálogo de productos
- `PEDIDO` - Órdenes de compra
- `CARRITO` - Detalle de productos por pedido
- `PAGO` - Registro de pagos (Tarjeta, Transferencia, Efectivo)
- `ENVIO` - Gestión de envíos
- `DEVOLUCION` - Control de devoluciones
- `DIRECCION` - Direcciones
- `TELEFONO` - Teléfonos de usuarios
- `AVASTECE` - Relación producto-proveedor

Ver `schema.sql` para más detalles.

---

## 🐳 Comandos Docker Útiles

```bash
# Ver logs
docker-compose logs -f

# Detener
docker-compose down

# Reiniciar
docker-compose restart

# Ver estado
docker-compose ps

# Acceder a MySQL
docker-compose exec mysql mysql -u ecommerce_user -pecommerce_pass ecommerce_db

# Eliminar todo (incluyendo datos)
docker-compose down -v

# Reconstruir
docker-compose up --build
```

---

## 🔧 Desarrollo

### Hacer cambios en el código

Si usas Docker, los cambios se reflejan automáticamente (modo debug activado).

### Agregar nuevas dependencias

```bash
# Agregar al requirements.txt
echo "nueva-libreria==1.0.0" >> requirements.txt

# Reconstruir contenedor
docker-compose down
docker-compose up --build
```

### Crear nuevas rutas

Editar `app.py` y agregar:

```python
@app.route('/nueva-ruta')
@login_required(roles=['Administrador'])
def nueva_funcion():
    return render_template('nueva_template.html')
```

---

## 📚 Documentación Adicional

- **Docker:** Ver `DOCKER_README.md`
- **Fase 1:** Ver `Bases de datos.pdf`
- **Fase 2:** Ver `Fase 2_ Final proyecto.pdf`

---

## 🐛 Solución de Problemas

### Puerto 5001 ocupado

```bash
# Cambiar puerto en docker-compose.yml o app.py
# O detener el proceso que usa el puerto:
lsof -ti:5001 | xargs kill -9
```

### MySQL no conecta

```bash
# Verificar que Docker esté corriendo
docker ps

# Ver logs de MySQL
docker-compose logs mysql

# Reiniciar
docker-compose restart mysql
```

### Error de contraseña en MySQL local

Usar Docker o resetear contraseña de MySQL:
```bash
brew services stop mysql
mysqld_safe --skip-grant-tables &
mysql -u root
# ALTER USER 'root'@'localhost' IDENTIFIED BY '';
```

---

## 🤝 Contribuir

1. Crear una rama nueva: `git checkout -b feature/nueva-funcionalidad`
2. Hacer commits: `git commit -m "Agregar nueva funcionalidad"`
3. Push: `git push origin feature/nueva-funcionalidad`
4. Crear Pull Request

---

## 📄 Licencia

Proyecto académico - Universidad Anáhuac Querétaro © 2025

---

## 📞 Contacto

Para dudas o problemas, contactar al equipo de desarrollo.

---

**¡Gracias por contribuir al proyecto! 🎉**
