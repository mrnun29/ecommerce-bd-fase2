# Sistema de Comercio Electrónico con Gestión de Inventarios

**Bases de Datos - Fase 2: Implementación**

## Equipo de Desarrollo
- Alberto Romero Mañón (00439959)
- Diego Nuñez Chavez (00516279)
- Emilio Antonio Tolosa Soto (00520630)
- Diego Vega Cabrera (00509910)

**Profesor:** Jonathan Omar Rendón Zamora  
**Universidad Anáhuac Querétaro**

## 📋 Descripción del Proyecto

Sistema integral de comercio electrónico desarrollado en Python con Flask que permite:

- Gestión de usuarios (Administradores, Empleados y Clientes)
- Control de inventarios con alertas de stock bajo
- Procesamiento de pedidos y pagos
- Gestión de proveedores y abastecimiento
- Sistema de envíos y devoluciones
- Reportes de ventas y análisis

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
- Python 3.8 o superior
- MySQL 8.0 o superior
- pip (gestor de paquetes Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
```bash
cd ecommerce_db
```

2. **Crear entorno virtual (recomendado)**
```bash
python3 -m venv venv
source venv/bin/activate  # En Mac/Linux
# venv\Scripts\activate  # En Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**
```bash
# Iniciar sesión en MySQL
mysql -u root -p

# Ejecutar el script de creación
source schema.sql
```

5. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tus credenciales de MySQL
```

6. **Ejecutar la aplicación**
```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 👥 Roles y Permisos

### Administrador
- Acceso completo al sistema
- Gestión de usuarios, productos, proveedores
- Reportes y estadísticas
- Eliminación de registros

### Empleado
- Gestión de inventarios
- Procesamiento de pedidos
- Gestión de envíos
- Registro de abastecimiento

### Cliente
- Visualización de productos
- Realización de compras
- Seguimiento de pedidos
- Gestión de devoluciones

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

## 📖 Uso del Sistema

### Primer Uso

1. Acceder a `http://localhost:5000/registro`
2. Crear una cuenta de usuario
3. Iniciar sesión con las credenciales
4. Explorar el dashboard según tu rol

### Crear Productos (Admin/Empleado)
1. Ir a `/productos/crear`
2. Llenar el formulario con datos del producto
3. El sistema validará stock mínimo automáticamente

### Realizar Pedido (Cliente)
1. Explorar catálogo de productos
2. Agregar productos al carrito
3. Proceder al checkout
4. Seleccionar método de pago
5. El stock se actualiza automáticamente

### Gestionar Proveedores (Admin/Empleado)
1. Ir a `/proveedores`
2. Registrar nuevo proveedor con dirección
3. Asociar productos mediante abastecimiento
4. El sistema actualiza stock al registrar abastecimientos

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
