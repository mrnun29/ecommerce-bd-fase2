# Guía del Proveedor

## Descripción del Rol

El **Proveedor** es el rol encargado de monitorear el inventario y registrar abastecimientos de productos. Este rol tiene permisos limitados y especializados, enfocados en la gestión de suministro de mercancía.

## Credenciales de Acceso

- **Correo:** `proveedor@ecommerce.com`
- **Contraseña:** `proveedor123`

## Permisos y Capacidades

El proveedor tiene acceso a las siguientes funcionalidades:

- Consultar inventario completo (solo lectura)
- Ver productos con stock bajo
- Registrar abastecimientos de productos
- Ver historial de abastecimientos propios
- Consultar detalles de productos
- **No puede:** Modificar productos
- **No puede:** Procesar ventas
- **No puede:** Ver pedidos de clientes
- **No puede:** Gestionar usuarios
- **No puede:** Modificar precios

## Vinculación con Empresa Proveedora

**Importante:** Para poder registrar abastecimientos, tu cuenta de usuario debe estar **vinculada a una empresa proveedora**.

### ¿Cómo saber si estoy vinculado?

Si puedes acceder a "Mi Historial" y ves el nombre de una empresa, estás vinculado correctamente.

## Funcionalidades Principales

### 1. Dashboard del Proveedor

Al iniciar sesión, verás tu panel personalizado con:

- Enlace a **Productos con Stock Bajo** (tu función principal)
- Botón para ver **Mi Historial de Abastecimientos**
- Consulta de **Inventario Completo**
- Información de tu empresa proveedora

**Ruta:** `/dashboard`

### 2. Consultar Inventario

#### 2.1 Ver Inventario Completo
- **Ruta:** `/inventario`
- Acceso de **solo lectura** a todos los productos
- Información mostrada:
  - Nombre del producto
  - Descripción
  - Precio actual
  - Stock disponible
  - Nivel mínimo de stock
  - Indicador visual de estado

#### 2.2 Indicadores Visuales
- **Verde:** Stock normal (por encima del nivel mínimo)
- **Rojo:** Stock bajo (por debajo del nivel mínimo) - ¡Requiere atención!

**¿Por qué es útil?**
- Monitoreas en tiempo real los niveles de stock
- Identificas productos que pronto necesitarán reabastecimiento
- Planificas tus entregas de manera proactiva

### 3. Productos con Stock Bajo

Esta es tu función **más importante** como proveedor.

#### 3.1 Acceder a Stock Bajo
- **Ruta:** `/proveedores/stock-bajo`
- Lista de productos que necesitan reabastecimiento urgente
- Ordenados por stock disponible (de menor a mayor)

#### 3.2 Interpretar la Lista

Cada producto muestra:
- **Nombre del producto**
- **Stock actual:** Cantidad disponible en este momento
- **Nivel mínimo:** Cantidad mínima que debería haber
- **Diferencia:** Cuántas unidades faltan para el nivel óptimo
- **Botón "Reabastecer":** Para registrar tu entrega

**Ejemplo:**
```
Producto: Laptop Dell Inspiron 15
Stock actual: 3 unidades
Nivel mínimo: 10 unidades
Alerta: ¡Necesita 7+ unidades!
```

#### 3.3 Priorización

**Alta prioridad (stock crítico):**
- Productos con 0-2 unidades
- Productos de alta demanda (consulta con administrador)

**Prioridad media:**
- Productos entre 3-5 unidades por debajo del mínimo

**Prioridad baja:**
- Productos cerca del nivel mínimo

### 4. Registrar Abastecimientos

Esta función te permite registrar las entregas de mercancía que realizas.

#### 4.1 Proceso de Abastecimiento

**Ruta:** `/proveedores/reabastecer` (POST)

**Pasos:**

1. **Identificar el producto a reabastecer**
   - Consulta la lista de stock bajo
   - Verifica que tienes el producto disponible para entregar

2. **Seleccionar el producto**
   - En la lista de stock bajo, localiza el producto
   - Verifica el nombre exacto

3. **Ingresar la cantidad**
   - Cantidad que estás entregando
   - Debe ser un número entero positivo
   - Ejemplo: 50, 100, 200

4. **Confirmar el abastecimiento**
   - Haz clic en "Reabastecer"
   - El sistema:
     - Validará tus permisos
     - Verificará que estés vinculado a una empresa
     - Actualizará el stock automáticamente
     - Registrará el abastecimiento en el historial
     - Mostrará confirmación

**Ejemplo de registro:**
```
Producto: Mouse Logitech M170
Stock antes: 2 unidades
Cantidad abastecida: 50 unidades
Stock después: 52 unidades
Proveedor: [Tu empresa]
Fecha: 2024-12-02 10:30:00
```

#### 4.2 Validaciones del Sistema

El sistema verifica automáticamente:
- Que estés autenticado como proveedor
- Que estés vinculado a una empresa proveedora
- Que el producto exista en el sistema
- Que la cantidad sea válida (mayor a 0)

Si algo falla, recibirás un mensaje de error explicativo.

### 5. Historial de Abastecimientos

#### 5.1 Ver Mi Historial
- **Ruta:** `/proveedor/historial`
- Lista completa de todos los abastecimientos que **tú** has registrado
- Ordenado por fecha (más reciente primero)

#### 5.2 Información Mostrada

Cada registro incluye:
- **Fecha y hora** del abastecimiento
- **Producto** abastecido (nombre completo)
- **Cantidad** entregada
- **Stock resultante** después del abastecimiento
- **Precio** del producto (referencia)

#### 5.3 Estadísticas del Historial

En la parte superior verás:
- **Total de abastecimientos** realizados
- **Total de unidades** entregadas
- **Nombre de tu empresa** proveedora

**Ejemplo de historial:**
```
Empresa: Distribuidora TechMX S.A. de C.V.
Total de abastecimientos: 15
Total de unidades entregadas: 1,250

Historial reciente:
1. Laptop Dell Inspiron 15 - 50 unidades - 2024-12-02 10:30
2. Mouse Logitech M170 - 100 unidades - 2024-12-01 15:45
3. Teclado Mecánico RGB - 75 unidades - 2024-11-30 09:15
...
```

#### 5.4 Usos del Historial

- **Trazabilidad:** Registro de todas tus entregas
- **Reportes:** Información para facturación
- **Auditoría:** Validación de cumplimiento de contratos
- **Planificación:** Análisis de patrones de reabastecimiento


---

**Versión:** 1.0  
**Última actualización:** Diciembre 2024  
**Sistema:** E-commerce con Gestión de Inventarios - Universidad Anáhuac Querétaro

