# Sistema de Comercio Electrónico con Gestión de Inventarios

**Bases de Datos - Fase 2: Implementación**

## Índice

1. [Equipo de Desarrollo](#-equipo-de-desarrollo)
2. [Descripción del Proyecto](#-descripción-del-proyecto)
3. [Arquitectura del Sistema](#-arquitectura-del-sistema)
4. [Base de Datos](#-base-de-datos)
5. [Instalación y Configuración](#-instalación-y-configuración)
6. [Usuarios de Prueba](#-usuarios-de-prueba)
7. [Documentación Detallada por Rol](#-documentación-detallada-por-rol)
8. [Uso del Sistema](#-uso-del-sistema)
9. [Seguridad](#-seguridad)
10. [Funcionalidades Principales](#-funcionalidades-principales)
11. [Consultas en Álgebra Relacional](#-consultas-en-álgebra-relacional-implementadas)
12. [Validaciones Implementadas](#-validaciones-implementadas)
13. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
14. [Flujo del Proceso](#-flujo-del-proceso)
15. [Puntos Extra Implementados](#-puntos-extra-implementados)
16. [Próximas Mejoras](#-próximas-mejoras)
17. [Soporte](#-soporte)

## Equipo de Desarrollo
- Alberto Romero Mañón (00439959)
- Diego Nuñez Chavez (00516279)
- Emilio Antonio Tolosa Soto (00520630)
- Diego Vega Cabrera (00509910)

**Profesor:** Jonathan Omar Rendón Zamora  
**Universidad Anáhuac Querétaro**

## Descripción del Proyecto

Sistema integral de comercio electrónico desarrollado con Flask y MySQL que implementa un modelo de 3 roles de usuario:

- **Administrador**: Gestión completa del sistema
- **Trabajador**: Procesamiento de ventas y gestión de inventario
- **Proveedor**: Consulta de inventario y registro de abastecimientos

### Funcionalidades Principales
- Sistema de autenticación con 3 roles diferenciados
- Control de inventarios con alertas de stock bajo
- Procesamiento de ventas directas (trabajadores)
- Gestión de proveedores con vinculación de usuarios
- Registro de abastecimientos por proveedores
- Sistema de pedidos y múltiples métodos de pago
- Interfaz web completa y responsiva

## Arquitectura del Sistema

```
ecommerce_db/
├── app.py                  # Aplicación principal Flask
├── schema_refactor.sql     # Script de creación de base de datos
├── requirements.txt        # Dependencias Python
├── docker-compose.yml      # Orquestación de contenedores
├── Dockerfile              # Imagen de Docker para Flask
├── config/
│   └── database.py        # Conexión a MySQL
├── models/
│   ├── usuario.py         # Modelo Usuario/Cliente
│   ├── producto.py        # Modelo Producto
│   ├── pedido.py          # Modelo Pedido y Pago
│   └── proveedor.py       # Modelo Proveedor
├── templates/             # Plantillas HTML completas
│   ├── index.html
│   ├── login.html
│   ├── dashboard_*.html
│   ├── productos/
│   ├── pedidos/
│   ├── proveedores/
│   └── ...
└── docs/                  # Documentación completa
    ├── README.md          # Índice de documentación
    ├── ADMINISTRADOR.md   # Guía del Administrador
    ├── TRABAJADOR.md      # Guía del Trabajador
    ├── PROVEEDOR.md       # Guía del Proveedor
    └── PUNTOS_EXTRAS_IMPLEMENTADOS.txt  # Puntos extra
```

## Base de Datos

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

## Instalación y Configuración

### Prerrequisitos
- Docker Desktop instalado ([Descargar aquí](https://www.docker.com/products/docker-desktop))
- Git (para clonar el repositorio)

### Instalación Rápida con Docker (RECOMENDADO)

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

 ¡Listo! El sistema está funcionando.

### Comandos Útiles

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

## Usuarios de Prueba

El sistema incluye 3 usuarios predefinidos, uno por cada rol:

### Administrador
- **Correo:** `admin@ecommerce.com`
- **Contraseña:** `admin123`
- **Permisos:**
  - Gestión completa de usuarios
  - CRUD de productos
  - Gestión de proveedores
  - Vincular/desvincular usuarios a empresas
  - Ver todos los pedidos
  - Eliminar registros

### Trabajador
- **Correo:** `trabajador@ecommerce.com`
- **Contraseña:** `123456`
- **Permisos:**
  - Procesar ventas directas
  - Gestionar inventario
  - Ver sus propios pedidos
  - Consultar productos

### Proveedor
- **Correo:** `proveedor@ecommerce.com`
- **Contraseña:** `123456`
- **Permisos:**
  - Consultar inventario (solo lectura)
  - Ver productos con stock bajo
  - Registrar abastecimientos
  - Ver historial de abastecimientos

## Seguridad

- Contraseñas encriptadas con Werkzeug
- Control de acceso basado en roles
- Validación de datos en front-end y back-end
- Protección contra inyección SQL (consultas parametrizadas)
- Sesiones seguras con Flask

## Funcionalidades Principales

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

## Consultas en Álgebra Relacional Implementadas

1. **Productos más vendidos**: Análisis de frecuencia en tabla CARRITO
2. **Pedidos por cliente**: Filtrado por id_cliente
3. **Stock bajo**: Comparación stock < nivel_minimo
4. **Ventas por periodo**: Suma de totales con filtro de fechas
5. **Proveedores por producto**: JOIN entre PRODUCTO y AVASTECE
6. **Gasto promedio**: AVG de total agrupado por cliente
7. **Ranking de ingresos**: SUM de ventas ordenado descendente

## Validaciones Implementadas

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

## Tecnologías Utilizadas

- **Backend**: Python 3.8+, Flask 3.0
- **Base de Datos**: MySQL 8.0
- **ORM/Conexión**: mysql-connector-python
- **Seguridad**: Werkzeug (hash de contraseñas)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3, JavaScript
- **Containerización**: Docker, Docker Compose
- **Control de Versiones**: Git, GitHub

## Documentación Detallada por Rol

Cada rol tiene su propia guía completa de usuario con instrucciones detalladas, casos de uso y mejores prácticas:

### [Guía del Administrador](docs/ADMINISTRADOR.md)
Documentación completa para administradores del sistema:
- Gestión de usuarios, productos y proveedores
- Panel de analíticas y reportes
- Control total del inventario
- Vinculación de proveedores
- Casos de uso y resolución de problemas

### [Guía del Trabajador](docs/TRABAJADOR.md)
Documentación para trabajadores/empleados:
- Procesar ventas en punto de venta
- Gestión de productos e inventario
- Ver y actualizar pedidos
- Procedimientos de turno (inicio, durante, fin)
- Checklists diarios y semanales

### [Guía del Proveedor](docs/PROVEEDOR.md)
Documentación para proveedores:
- Consultar inventario y stock bajo
- Registrar abastecimientos
- Historial de entregas
- Rutinas diarias y mensuales
- Generación de reportes para facturación

## Uso del Sistema

### Iniciar Sesión

1. Acceder a `http://localhost:5001`
2. Usar cualquiera de las credenciales de prueba (ver sección "Usuarios de Prueba")
3. El sistema te redirigirá al dashboard correspondiente a tu rol
4. **Consulta la guía de tu rol** en la carpeta `docs/` para instrucciones detalladas

### Como Administrador

**Para una guía completa, consulta [docs/ADMINISTRADOR.md](docs/ADMINISTRADOR.md)**

**Funciones principales:**
- Gestión completa de productos (CRUD)
- Administración de usuarios (crear, editar, inhabilitar, eliminar)
- Gestión de proveedores y vinculación de usuarios
- Panel de analíticas con reportes en tiempo real
- Control de inventario con alertas automáticas
- Visualización de todos los pedidos del sistema

### Como Trabajador

**Para una guía completa, consulta [docs/TRABAJADOR.md](docs/TRABAJADOR.md)**

**Funciones principales:**
- Procesar ventas directas en punto de venta
- Gestionar catálogo de productos (crear/editar)
- Consultar y actualizar inventario
- Ver y actualizar estado de pedidos procesados
- Identificar productos con stock bajo

### Como Proveedor

**Para una guía completa, consulta [docs/PROVEEDOR.md](docs/PROVEEDOR.md)**

**Funciones principales:**
- Consultar inventario completo (solo lectura)
- Monitorear productos con stock bajo
- Registrar abastecimientos de mercancía
- Ver historial detallado de entregas
- Generar reportes para facturación

## Flujo del Proceso

1. **Cliente realiza pedido** → Valida stock
2. **Sistema confirma pedido** → Genera registro en PEDIDO
3. **Cliente realiza pago** → Registro en PAGO (especialización)
4. **Sistema procesa envío** → Registro en ENVIO
5. **Descuento de inventario** → UPDATE en PRODUCTO
6. **Alerta de stock bajo** → Si stock < nivel_minimo
7. **Orden automática** → Registro en AVASTECE con proveedor

## Contribuciones

Este proyecto es parte del curso de Bases de Datos. Para mejoras o sugerencias:

1. Crear un issue describiendo la mejora
2. Fork del repositorio
3. Crear una rama para la feature
4. Commit de cambios
5. Pull request con descripción detallada

## Licencia

Proyecto académico - Universidad Anáhuac Querétaro © 2025

## Puntos Extra Implementados

El sistema incluye múltiples puntos extra que superan los requisitos base del proyecto. Para detalles completos, consulta [PUNTOS_EXTRAS_IMPLEMENTADOS.txt](docs/PUNTOS_EXTRAS_IMPLEMENTADOS.txt):

1. **Reportes con Información Cruzada (5 pts)**: Panel de analíticas con JOINs múltiples
2. **Volumen de Datos (10 pts)**: 1010 productos, 1000 pedidos generados automáticamente
3. **Seguridad para Accesos Simultáneos (10 pts)**: Transacciones InnoDB con commit/rollback
4. **Integridad y Protección ante Ataques (10 pts)**: Queries parametrizadas, hash de contraseñas
5. **Escalabilidad y Desempeño (15 pts)**: Índices optimizados, queries eficientes
6. **Bitácora (Log) de Operaciones (5 pts)**: Logging completo con timestamps
7. **Dockerización del Sistema (10 pts)**: Docker Compose con 2 servicios
8. **Arquitectura Desacoplada (10 pts)**: Patrón MVC con capas separadas
9. **Control de Versiones (5 pts)**: Git/GitHub con commits descriptivos
10. **Diseño Responsivo (5 pts)**: Bootstrap 5.3 con modo oscuro

**Total de puntos extra: 85 puntos**

**Fecha de Entrega:** Fase 2 - 2025  
**Materia:** Bases de Datos  
**Universidad Anáhuac Querétaro**
