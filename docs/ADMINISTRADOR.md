# Guía del Administrador

## Descripción del Rol

El **Administrador** tiene control total sobre el sistema de comercio electrónico. Este rol está diseñado para gestionar toda la operación del negocio, desde el inventario hasta los usuarios y proveedores.

## Credenciales de Acceso

- **Correo:** `admin@ecommerce.com`
- **Contraseña:** `admin123`

## Permisos y Capacidades

El administrador tiene acceso completo a todas las funcionalidades del sistema:

- Gestión completa de usuarios (crear, editar, inhabilitar, eliminar)
- CRUD completo de productos
- Gestión de proveedores (empresas)
- Vincular/desvincular usuarios a empresas proveedoras
- Visualizar todos los pedidos del sistema
- Acceso a analíticas y reportes
- Gestión de inventario con alertas de stock bajo
- Eliminar cualquier registro del sistema

## Funcionalidades Principales

### 1. Dashboard Principal

Al iniciar sesión, accederás al dashboard del administrador con acceso rápido a:

- Estadísticas generales del sistema
- Accesos directos a gestión de productos, usuarios y proveedores
- Panel de analíticas y reportes
- Gestión de inventario

**Ruta:** `/dashboard`

### 2. Gestión de Productos

#### 2.1 Ver Catálogo Completo
- **Ruta:** `/productos`
- Visualiza todos los productos del sistema
- Información mostrada: nombre, descripción, precio, stock actual, nivel mínimo
- Identificación visual de productos con stock bajo (destacados en rojo)

#### 2.2 Crear Nuevo Producto
- **Ruta:** `/productos/crear`
- **Campos requeridos:**
  - Nombre del producto (máx. 40 caracteres)
  - Descripción (máx. 200 caracteres)
  - Precio (formato decimal, ej. 299.99)
  - Stock inicial (número entero)
  - Nivel mínimo de stock (por defecto: 10)
  - URL de imagen (opcional)

**Ejemplo de creación:**
```
Nombre: Laptop Dell Inspiron 15
Descripción: Laptop con procesador Intel i5, 8GB RAM, 256GB SSD
Precio: 12999.00
Stock: 50
Nivel Mínimo: 5
Imagen: https://ejemplo.com/imagen-laptop.jpg
```

#### 2.3 Editar Producto Existente
- **Ruta:** `/productos/<id>/editar`
- Permite modificar cualquier campo del producto
- Actualizar stock manualmente si es necesario
- Ajustar nivel mínimo según demanda

#### 2.4 Eliminar Producto
- **Ruta:** `/productos/<id>/eliminar` (POST)
- **Precaución:** Esta acción eliminará el producto permanentemente
- Solo posible si el producto no está en pedidos activos

### 3. Gestión de Usuarios

#### 3.1 Ver Lista de Usuarios
- **Ruta:** `/usuarios`
- Visualiza todos los usuarios del sistema
- Filtrado por rol: Administrador, Trabajador, Proveedor, Cliente
- Estado: Activo o Inhabilitado

#### 3.2 Crear Nuevo Usuario
- **Ruta:** `/usuarios/crear`
- **Campos requeridos:**
  - Nombre completo
  - Correo electrónico (único en el sistema)
  - Contraseña
  - Rol: Trabajador, Proveedor o Cliente
  - Dirección completa (calle, número, ciudad, código postal)

**Ejemplo de creación de trabajador:**
```
Nombre: Juan Pérez García
Correo: juan.perez@ecommerce.com
Contraseña: seguridadPass123
Rol: Trabajador
Calle: Av. Constituyentes
Número: 123
Ciudad: Querétaro
Código Postal: 76000
```

#### 3.3 Editar Usuario
- **Ruta:** `/usuarios/<id>/editar` (POST)
- Modificar información personal y dirección
- Cambiar rol si es necesario
- No puedes editar tu propia cuenta de administrador

#### 3.4 Inhabilitar Usuario
- **Ruta:** `/usuarios/<id>/inhabilitar` (POST)
- Deshabilita el acceso del usuario sin eliminar sus datos
- El usuario no podrá iniciar sesión
- Mantiene historial de pedidos y transacciones
- **Ventaja:** Reversible - puedes reactivar la cuenta después

#### 3.5 Habilitar Usuario
- **Ruta:** `/usuarios/<id>/habilitar` (POST)
- Reactiva una cuenta previamente inhabilitada
- El usuario podrá iniciar sesión nuevamente

#### 3.6 Eliminar Usuario
- **Ruta:** `/usuarios/<id>/eliminar` (POST)
- **Precaución:** Elimina permanentemente el usuario
- Elimina también su dirección y teléfonos asociados
- No puedes eliminar tu propia cuenta de administrador

### 4. Gestión de Proveedores

#### 4.1 Ver Lista de Proveedores
- **Ruta:** `/proveedores`
- Visualiza todas las empresas proveedoras registradas
- Muestra usuarios vinculados a cada empresa
- Lista de usuarios disponibles para vincular

#### 4.2 Crear Nuevo Proveedor (Empresa)
- **Ruta:** `/proveedores/crear`
- **Campos requeridos:**
  - Nombre de la empresa
  - Nombre del contacto
  - Teléfono
  - Dirección completa (calle, número, ciudad, código postal)

**Ejemplo:**
```
Empresa: Distribuidora TechMX S.A. de C.V.
Contacto: María López Sánchez
Teléfono: 442-123-4567
Calle: Blvd. Bernardo Quintana
Número: 4100
Ciudad: Querétaro
Código Postal: 76140
```

#### 4.3 Vincular Usuario a Proveedor
- **Ruta:** `/proveedores/<id_proveedor>/vincular` (POST)
- Selecciona un usuario con rol "Proveedor" sin asignar
- El usuario podrá gestionar abastecimientos para esa empresa
- **Requisito:** El usuario debe tener rol "Proveedor"

**Proceso:**
1. Crea un usuario con rol "Proveedor" (si no existe)
2. En la lista de proveedores, busca la empresa
3. Haz clic en "Vincular Usuario"
4. Selecciona el usuario de la lista desplegable
5. Confirma la vinculación

#### 4.4 Desvincular Usuario de Proveedor
- **Ruta:** `/proveedores/<id_proveedor>/desvincular/<id_usuario>` (POST)
- Remueve la asociación entre usuario y empresa
- El usuario ya no podrá registrar abastecimientos
- Los abastecimientos previos se mantienen en el historial

#### 4.5 Eliminar Proveedor
- **Ruta:** `/proveedores/<id>/eliminar` (POST)
- Elimina la empresa proveedora permanentemente
- Elimina también el historial de abastecimientos
- Los usuarios vinculados quedan disponibles para reasignar

### 5. Gestión de Inventario

#### 5.1 Ver Inventario Completo
- **Ruta:** `/inventario`
- Tabla con todos los productos y sus niveles de stock
- Indicadores visuales:
  - Verde: Stock normal (por encima del nivel mínimo)
  - Rojo: Stock bajo (por debajo del nivel mínimo)
- Búsqueda y filtrado de productos

#### 5.2 Editar Inventario
- **Ruta:** `/inventario/<id_producto>/editar`
- Ajustar stock manualmente
- Modificar nivel mínimo de alerta
- Actualizar precio del producto

#### 5.3 Ver Productos con Stock Bajo
- **Ruta:** `/proveedores/stock-bajo`
- Lista de productos que necesitan reabastecimiento urgente
- Ordenados por stock disponible (menor a mayor)
- Opción para reabastecer directamente

#### 5.4 Reabastecer Producto
- **Ruta:** `/proveedores/reabastecer` (POST)
- Selecciona el producto a reabastecer
- Selecciona el proveedor que abastecerá
- Ingresa la cantidad a añadir al stock
- El sistema actualizará automáticamente el inventario

**Ejemplo:**
```
Producto: Laptop Dell Inspiron 15 (Stock actual: 3)
Proveedor: Distribuidora TechMX
Cantidad a reabastecer: 50
Nuevo stock: 53
```

### 6. Gestión de Pedidos

#### 6.1 Ver Todos los Pedidos
- **Ruta:** `/pedidos`
- Visualiza todos los pedidos del sistema
- Información mostrada:
  - ID del pedido
  - Cliente que realizó el pedido
  - Trabajador que procesó la venta (si aplica)
  - Total del pedido
  - Estado: Pendiente, Procesando, Enviado, Entregado, Cancelado
  - Fecha de creación

#### 6.2 Ver Detalle de Pedido
- **Ruta:** `/pedidos/<id>`
- Información completa del pedido:
  - Lista de productos con cantidades
  - Precios unitarios y subtotales
  - Información de pago (tipo, monto, detalles)
  - Estado actual
  - Cliente y trabajador asociados

#### 6.3 Actualizar Estado de Pedido
- **Ruta:** `/pedidos/<id_pedido>/actualizar` (POST)
- Cambiar estado del pedido según el flujo:
  - **Pendiente** → Recién creado, esperando procesamiento
  - **Procesando** → En preparación
  - **Enviado** → En tránsito al cliente
  - **Entregado** → Completado exitosamente
  - **Cancelado** → Pedido cancelado

### 7. Panel de Analíticas

#### 7.1 Acceder a Analíticas
- **Ruta:** `/admin/analiticas`
- Dashboard con métricas del negocio

#### 7.2 Métricas Disponibles

**A. Ventas del Mes**
- Total de ingresos en los últimos 30 días
- Comparación con periodos anteriores

**B. Productos Más Vendidos (Top 10)**
- Ranking de productos por unidades vendidas
- Ingresos totales generados por producto
- Stock actual de cada producto

**C. Ventas por Trabajador**
- Número de ventas procesadas por cada trabajador
- Total de ingresos generados
- Promedio de venta por trabajador

**D. Pedidos Recientes**
- Últimos 10 pedidos realizados
- Estado actual de cada uno
- Acceso directo a los detalles

**E. Productos con Stock Bajo**
- Alerta de productos que necesitan reabastecimiento
- Nivel actual vs. nivel mínimo
- Enlace directo para reabastecer

### 8. APIs y Búsquedas

El sistema expone endpoints API para consultas avanzadas:

#### 8.1 Buscar Productos
- **Ruta:** `/api/productos/buscar?q=termino`
- Búsqueda por nombre o descripción
- Retorna JSON con productos coincidentes

#### 8.2 Productos con Stock Bajo
- **Ruta:** `/api/productos/stock-bajo`
- Retorna JSON con productos bajo nivel mínimo

#### 8.3 Pedidos por Estado
- **Ruta:** `/api/pedidos/estados`
- Conteo de pedidos agrupados por estado
- Retorna JSON con estadísticas

#### 8.4 Top 10 Clientes
- **Ruta:** `/api/clientes/top10`
- Clientes con más pedidos realizados
- Total gastado por cliente

## Casos de Uso Comunes

### Caso 1: Agregar Nuevo Producto al Catálogo

1. Ir a **Dashboard** → **Productos** → **Crear Producto**
2. Llenar el formulario con los datos del producto
3. Establecer stock inicial y nivel mínimo
4. Guardar
5. El producto aparecerá inmediatamente en el catálogo

### Caso 2: Dar de Alta un Nuevo Trabajador

1. Ir a **Dashboard** → **Usuarios** → **Crear Usuario**
2. Llenar datos personales y dirección
3. Seleccionar rol "Trabajador"
4. Establecer contraseña inicial
5. Guardar
6. Notificar al trabajador sus credenciales de acceso

### Caso 3: Configurar Proveedor para Abastecimientos

1. **Crear la empresa proveedora:**
   - Ir a **Proveedores** → **Crear Proveedor**
   - Llenar datos de la empresa

2. **Crear usuario para el proveedor:**
   - Ir a **Usuarios** → **Crear Usuario**
   - Seleccionar rol "Proveedor"

3. **Vincular usuario a la empresa:**
   - En **Lista de Proveedores**, localizar la empresa
   - Clic en "Vincular Usuario"
   - Seleccionar el usuario creado
   - Confirmar

4. El usuario proveedor ya puede registrar abastecimientos

### Caso 4: Responder a Alerta de Stock Bajo

1. Ir a **Dashboard** → **Inventario** o **Stock Bajo**
2. Identificar productos en rojo (por debajo del mínimo)
3. Clic en "Reabastecer"
4. Seleccionar proveedor que abastecerá
5. Ingresar cantidad
6. Confirmar
7. El stock se actualiza automáticamente

### Caso 5: Monitorear Desempeño del Negocio

1. Ir a **Dashboard** → **Analíticas**
2. Revisar:
   - Ventas del mes
   - Productos más vendidos
   - Desempeño de trabajadores
   - Pedidos recientes y sus estados
3. Identificar áreas de mejora
4. Tomar decisiones basadas en datos

### Caso 6: Inhabilitar Usuario Temporalmente

1. Ir a **Usuarios**
2. Localizar el usuario
3. Clic en "Inhabilitar"
4. El usuario no podrá iniciar sesión
5. Para reactivar: clic en "Habilitar"

## Precauciones y Buenas Prácticas

### Seguridad
- **Nunca compartas las credenciales de administrador**
- Cambia la contraseña por defecto inmediatamente
- Revisa periódicamente los usuarios activos
- Inhabilita usuarios inactivos en lugar de eliminarlos
- Mantén un registro de cambios importantes

### Gestión de Inventario
- Establece niveles mínimos realistas según la demanda
- Revisa semanalmente los productos con stock bajo
- Mantén contacto con proveedores para abastecimientos rápidos
- Actualiza precios según el mercado

### Gestión de Usuarios
- Asigna roles correctamente según las responsabilidades
- Verifica que los trabajadores solo procesen ventas autorizadas
- Vincula proveedores a empresas reales para trazabilidad
- No elimines usuarios con historial de transacciones (inhabilítalos)

### Gestión de Pedidos
- Actualiza estados de pedidos oportunamente
- Verifica que el stock se descuente correctamente
- Revisa pedidos cancelados para identificar problemas
- Mantén comunicación con clientes sobre entregas


## Reportes y Consultas SQL Implementadas

El sistema ejecuta las siguientes consultas en segundo plano:

1. **Productos más vendidos:** JOIN entre PRODUCTO, CARRITO y PEDIDO
2. **Ventas por trabajador:** Agrupación de PEDIDO por `procesado_por`
3. **Stock bajo:** Comparación `stock < nivel_minimo`
4. **Total de ventas del mes:** SUM de totales con filtro de fecha
5. **Ranking de ingresos:** JOIN con agregación por producto
6. **Top clientes:** Agrupación por `id_usuario` con COUNT de pedidos


---

**Versión:** 1.0  
**Última actualización:** Diciembre 2024  
**Sistema:** E-commerce con Gestión de Inventarios - Universidad Anáhuac Querétaro
