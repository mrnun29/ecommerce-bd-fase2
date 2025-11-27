# 🛒 Sistema de Comercio Electrónico con Gestión de Inventarios

**Bases de Datos - Fase 2: Implementación**

## 👥 Equipo de Desarrollo
- Alberto Romero Mañón (00439959)
- Diego Nuñez Chavez (00516279)
- Emilio Antonio Tolosa Soto (00520630)
- Diego Vega Cabrera (00509910)

**Profesor:** Jonathan Omar Rendón Zamora  
**Universidad Anáhuac Querétaro**

## 📋 Descripción del Proyecto

Sistema integral de comercio electrónico desarrollado con Flask y MySQL que implementa un modelo de 3 roles de usuario:

- **Administrador**: Gestión completa del sistema
- **Trabajador**: Procesamiento de ventas y gestión de inventario
- **Proveedor**: Consulta de inventario y registro de abastecimientos

### Funcionalidades Principales
- ✅ Sistema de autenticación con 3 roles diferenciados
- ✅ Control de inventarios con alertas de stock bajo
- ✅ Procesamiento de ventas directas (trabajadores)
- ✅ Gestión de proveedores con vinculación de usuarios
- ✅ Registro de abastecimientos por proveedores
- ✅ Sistema de pedidos y múltiples métodos de pago
- ✅ Interfaz web completa y responsiva

## 🏗️ Arquitectura del Sistema

```
ecommerce_db/
├── app.py                  # Aplicación principal Flask
├── schema.sql              # Script de creación de base de datos
├── requirements.txt        # Dependencias Python
├── .env.example           # Configuración de ejemplo
├── config/
│   └── database.py        # Conexión a MySQL
├── models/
│   ├── usuario.py         # Modelo Usuario/Cliente
│   ├── producto.py        # Modelo Producto
│   ├── pedido.py          # Modelo Pedido y Pago
│   └── proveedor.py       # Modelo Proveedor
└── templates/             # Plantillas HTML (a crear)
    ├── index.html
    ├── login.html
    ├── registro.html
    ├── productos/
    ├── pedidos/
    └── proveedores/
```

## 🗄️ Base de Datos

El sistema utiliza MySQL con las siguientes entidades principales:

### Tablas Principales
- **USUARIO**: Gestión de usuarios del sistema
- **CLIENTE**: Información específica de clientes
- **PROVEEDOR**: Datos de proveedores
- **PRODUCTO**: Catálogo de productos con control de stock
- **PEDIDO**: Órdenes de compra
- **CARRITO**: Detalle de productos por pedido
- **PAGO**: Registro de pagos (con especialización en Tarjeta, Transferencia, Efectivo)
- **ENVIO**: Gestión de envíos
- **DEVOLUCION**: Control de devoluciones
- **AVASTECE**: Relación producto-proveedor

## 🚀 Instalación y Configuración

### Prerrequisitos
- Docker Desktop instalado ([Descargar aquí](https://www.docker.com/products/docker-desktop))
- Git (para clonar el repositorio)

### 👉 Instalación Rápida con Docker (RECOMENDADO)

**Paso 1: Clonar el repositorio**
```bash
git clone https://github.com/mrnun29/ecommerce-bd-fase2.git
cd ecommerce-bd-fase2
```

**Paso 2: Iniciar los contenedores**
```bash
docker-compose up -d
```

Esto creará:
- Contenedor MySQL en el puerto `3306`
- Contenedor Flask en el puerto `5001`
- Aplicará automáticamente el schema y datos de prueba

**Paso 3: Acceder a la aplicación**

Abre tu navegador en: **http://localhost:5001**

🎉 ¡Listo! El sistema está funcionando.

### 🔄 Comandos Útiles

**Reiniciar el servidor (después de cambios en el código):**
```bash
./reiniciar.sh
```

**Ver logs del servidor:**
```bash
docker logs ecommerce_web
```

**Detener los contenedores:**
```bash
docker-compose down
```

**Reiniciar todo desde cero:**
```bash
docker-compose down -v  # Elimina volúmenes
docker-compose up -d
```

## 👥 Usuarios de Prueba

El sistema incluye 3 usuarios predefinidos, uno por cada rol:

### 🔑 Administrador
- **Correo:** `admin@ecommerce.com`
- **Contraseña:** `admin123`
- **Permisos:**
  - ✅ Gestión completa de usuarios
  - ✅ CRUD de productos
  - ✅ Gestión de proveedores
  - ✅ Vincular/desvincular usuarios a empresas
  - ✅ Ver todos los pedidos
  - ✅ Eliminar registros

### 🛠️ Trabajador
- **Correo:** `trabajador@ecommerce.com`
- **Contraseña:** `123456`
- **Permisos:**
  - ✅ Procesar ventas directas
  - ✅ Gestionar inventario
  - ✅ Ver sus propios pedidos
  - ✅ Consultar productos

### 🚚 Proveedor
- **Correo:** `proveedor@ecommerce.com`
- **Contraseña:** `123456`
- **Permisos:**
  - ✅ Consultar inventario (solo lectura)
  - ✅ Ver productos con stock bajo
  - ✅ Registrar abastecimientos
  - ✅ Ver historial de abastecimientos

## 🔐 Seguridad

- Contraseñas encriptadas con Werkzeug
- Control de acceso basado en roles
- Validación de datos en front-end y back-end
- Protección contra inyección SQL (consultas parametrizadas)
- Sesiones seguras con Flask

## 📊 Funcionalidades Principales

### Gestión de Productos
- CRUD completo de productos
- Control de stock con alertas
- Búsqueda y filtrado
- Historial de abastecimiento
- Productos más vendidos

### Gestión de Pedidos
- Creación de pedidos con múltiples productos
- Cálculo automático de totales
- Estados: Pendiente, Procesando, Enviado, Entregado, Cancelado
- Actualización automática de inventario
- Historial por cliente

### Sistema de Pagos
- Múltiples métodos de pago:
  - Tarjeta (con datos bancarios)
  - Transferencia (con referencia)
  - Efectivo (con folio y fecha límite)

### Gestión de Proveedores
- Registro de proveedores con dirección
- Relación con productos abastecidos
- Registro de abastecimientos
- Actualización automática de stock

### Reportes y Consultas
- Productos más vendidos
- Ranking de productos por ingresos
- Total de ventas por periodo
- Gasto promedio por cliente
- Productos con stock bajo
- Historial de compras

## 🔧 Consultas en Álgebra Relacional Implementadas

1. **Productos más vendidos**: Análisis de frecuencia en tabla CARRITO
2. **Pedidos por cliente**: Filtrado por id_cliente
3. **Stock bajo**: Comparación stock < nivel_minimo
4. **Ventas por periodo**: Suma de totales con filtro de fechas
5. **Proveedores por producto**: JOIN entre PRODUCTO y AVASTECE
6. **Gasto promedio**: AVG de total agrupado por cliente
7. **Ranking de ingresos**: SUM de ventas ordenado descendente

## 📝 Validaciones Implementadas

### Front-end
- Campos obligatorios (NOT NULL)
- Formatos válidos (email, teléfono, fechas)
- Límites de caracteres (VARCHAR)
- Validación de tipos de datos

### Back-end
- Verificación de llaves foráneas
- Validación de stock disponible
- Verificación de estado de pedido
- Validación de montos y fechas
- Prevención de registros huérfanos

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.8+, Flask 3.0
- **Base de Datos**: MySQL 8.0
- **ORM/Conexión**: mysql-connector-python
- **Seguridad**: Werkzeug (hash de contraseñas)
- **Frontend**: HTML5, CSS3, JavaScript (a implementar)

## 📚 Uso del Sistema

### 1️⃣ Iniciar Sesión

1. Acceder a `http://localhost:5001`
2. Usar cualquiera de las credenciales de prueba
3. El sistema te redirigirá al dashboard correspondiente a tu rol

### 2️⃣ Como Administrador

**Gestionar Productos:**
- Dashboard → Productos → Crear Producto
- Llenar formulario con nombre, precio, stock, etc.
- El producto aparecerá en el catálogo

**Gestionar Usuarios:**
- Dashboard → Proveedores y Trabajadores
- Ver lista de trabajadores y proveedores
- Editar o eliminar usuarios (botón de lápiz/basura)
- Crear nuevos trabajadores o proveedores

**Vincular Usuarios a Proveedores:**
- Dashboard → Proveedores (lista)
- Clic en "Vincular Usuario" en cada empresa
- Seleccionar usuario proveedor sin vincular
- El usuario ahora puede registrar abastecimientos

### 3️⃣ Como Trabajador

**Procesar Ventas:**
- Dashboard → Procesar Ventas
- Seleccionar productos del dropdown
- Ingresar cantidades
- Elegir método de pago (Efectivo/Tarjeta/Transferencia)
- Clic en "Procesar Venta"
- El inventario se actualiza automáticamente

**Ver Pedidos:**
- Dashboard → Mis Pedidos
- Ver historial de ventas procesadas

### 4️⃣ Como Proveedor

**Ver Stock Bajo:**
- Dashboard → Productos con Stock Bajo
- Identificar productos que necesitan reabastecimiento

**Registrar Abastecimiento:**
- Seleccionar producto con stock bajo
- Ingresar cantidad a reabastecer
- Clic en "Reabastecer"
- El stock se actualiza automáticamente

**Ver Historial:**
- Dashboard → Mi Historial
- Consultar todos los abastecimientos realizados

## 🔄 Flujo del Proceso

1. **Cliente realiza pedido** → Valida stock
2. **Sistema confirma pedido** → Genera registro en PEDIDO
3. **Cliente realiza pago** → Registro en PAGO (especialización)
4. **Sistema procesa envío** → Registro en ENVIO
5. **Descuento de inventario** → UPDATE en PRODUCTO
6. **Alerta de stock bajo** → Si stock < nivel_minimo
7. **Orden automática** → Registro en AVASTECE con proveedor

## 🤝 Contribuciones

Este proyecto es parte del curso de Bases de Datos. Para mejoras o sugerencias:

1. Crear un issue describiendo la mejora
2. Fork del repositorio
3. Crear una rama para la feature
4. Commit de cambios
5. Pull request con descripción detallada

## 📄 Licencia

Proyecto académico - Universidad Anáhuac Querétaro © 2025

## 📞 Soporte

Para preguntas o problemas:
- Consultar documentación de la Fase 1 (Modelos ER/ERE)
- Revisar el código de los modelos para consultas SQL
- Contactar al equipo de desarrollo

## 🎯 Próximas Mejoras

- [ ] Interfaz web completa con Bootstrap
- [ ] API REST para integración móvil
- [ ] Sistema de notificaciones por email
- [ ] Dashboard con gráficas de análisis
- [ ] Exportación de reportes a PDF/Excel
- [ ] Carrito de compras persistente
- [ ] Sistema de reseñas y valoraciones
- [ ] Integración con pasarelas de pago reales

---

**Fecha de Entrega:** Fase 2 - 2025  
**Materia:** Bases de Datos  
**Universidad Anáhuac Querétaro**
