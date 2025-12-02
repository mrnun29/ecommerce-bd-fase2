# Guía del Trabajador

## Descripción del Rol

El **Trabajador** (o Empleado) es el rol encargado de procesar ventas directas en el punto de venta, gestionar el inventario y atender las operaciones diarias del comercio. Este rol tiene permisos intermedios enfocados en las operaciones de venta.

## Credenciales de Acceso

- **Correo:** `trabajador@ecommerce.com`
- **Contraseña:** `123456`

## Permisos y Capacidades

El trabajador tiene acceso a las siguientes funcionalidades:

- Procesar ventas directas (punto de venta)
- Consultar catálogo de productos
- Ver y gestionar inventario
- Crear y editar productos
- Ver sus propios pedidos procesados
- Actualizar estado de pedidos
- **No puede:** Crear/eliminar usuarios
- **No puede:** Gestionar proveedores
- **No puede:** Ver analíticas completas del sistema

## Funcionalidades Principales

### 1. Dashboard del Trabajador

Al iniciar sesión, verás tu panel personalizado con:

- Acceso rápido a **Procesar Ventas**
- Enlace a **Gestionar Productos**
- Botón para ver **Mis Pedidos**
- Consulta de **Inventario**

**Ruta:** `/dashboard`

### 2. Procesar Ventas (Punto de Venta)

Esta es la función principal del trabajador: registrar ventas directas a clientes.

#### 2.1 Acceder al Punto de Venta
- **Ruta:** `/ventas`
- Interfaz simplificada para ventas rápidas

#### 2.2 Crear una Venta

**Paso 1: Seleccionar Productos**
1. En el formulario, verás un selector de productos
2. Cada producto muestra:
   - Nombre completo
   - Precio unitario
   - Stock disponible
3. Selecciona el producto de la lista desplegable
4. Ingresa la cantidad deseada

**Paso 2: Agregar Más Productos (Opcional)**
- Puedes agregar múltiples productos a la misma venta
- Usa el botón "+" para añadir más líneas de productos
- El sistema calculará automáticamente el total

**Paso 3: Seleccionar Método de Pago**
Opciones disponibles:
- **Efectivo:** Pago en efectivo en caja
- **Tarjeta:** Pago con tarjeta de crédito/débito
- **Transferencia:** Pago mediante transferencia bancaria

**Paso 4: Procesar la Venta**
1. Revisa que todos los productos y cantidades sean correctos
2. Verifica el método de pago
3. Haz clic en "Procesar Venta"
4. El sistema:
   - Validará que hay stock suficiente
   - Creará el pedido automáticamente
   - Registrará el pago
   - Descontará el stock del inventario
   - Generará un número de pedido

**Ejemplo de Venta:**
```
Cliente: Venta directa
Productos:
  - Laptop Dell Inspiron 15 (Cantidad: 1) → $12,999.00
  - Mouse Logitech M170 (Cantidad: 2) → $399.00 c/u
  
Subtotal: $13,797.00
Total: $13,797.00
Método de pago: Efectivo
```

#### 2.3 Confirmación de Venta
Después de procesar, verás:
- Número de pedido generado
- Detalles completos de la venta
- Comprobante para entregar al cliente

**Ruta del comprobante:** `/pedidos/<id_pedido>`

### 3. Gestión de Productos

Como trabajador, puedes gestionar el catálogo de productos.

#### 3.1 Ver Catálogo de Productos
- **Ruta:** `/productos`
- Lista completa de productos disponibles
- Información: nombre, precio, stock, descripción
- Indicadores visuales:
  - Verde: Stock normal
  - Rojo: Stock bajo (requiere atención)

#### 3.2 Crear Nuevo Producto
- **Ruta:** `/productos/crear`
- Útil cuando llega mercancía nueva

**Campos a llenar:**
- **Nombre:** Nombre descriptivo del producto (máx. 40 caracteres)
- **Descripción:** Detalles del producto (máx. 200 caracteres)
- **Precio:** Precio de venta (formato: 299.99)
- **Stock:** Cantidad inicial disponible
- **Nivel Mínimo:** Alerta cuando el stock baje de este número (sugerido: 10)
- **Imagen:** URL de la imagen del producto (opcional)

**Ejemplo:**
```
Nombre: Teclado Mecánico RGB
Descripción: Teclado gaming mecánico con iluminación RGB, switches rojos
Precio: 899.00
Stock: 25
Nivel Mínimo: 5
Imagen: https://ejemplo.com/teclado.jpg
```

#### 3.3 Editar Producto
- **Ruta:** `/productos/<id>/editar`
- Actualizar información del producto
- Ajustar precios según instrucciones
- Corregir stock si es necesario

**Casos de uso:**
- Actualizar precio por cambio de lista
- Corregir stock después de inventario físico
- Mejorar descripción del producto
- Cambiar imagen

#### 3.4 Ver Detalle de Producto
- **Ruta:** `/productos/<id>`
- Información completa del producto
- Historial de abastecimientos (si aplica)
- Stock actual vs. nivel mínimo

### 4. Gestión de Inventario

#### 4.1 Consultar Inventario
- **Ruta:** `/productos` o `/inventario`
- Vista de todos los productos con sus niveles de stock
- Alertas visuales para productos con stock bajo

#### 4.2 Identificar Productos con Stock Bajo
Los productos con `stock < nivel_minimo` aparecen destacados en **rojo**.

**Acción recomendada:**
1. Identifica el producto con stock bajo
2. Notifica al administrador o proveedor
3. Si tienes mercancía en almacén, actualiza el stock manualmente

#### 4.3 Actualizar Stock Manualmente
Si necesitas ajustar el stock (por ejemplo, después de un inventario físico):
1. Ve a **Productos** → **Editar Producto**
2. Modifica el campo "Stock"
3. Guarda los cambios

**Precaución:** Solo ajusta el stock si tienes certeza de las cantidades físicas.

### 5. Gestión de Pedidos

#### 5.1 Ver Mis Pedidos
- **Ruta:** `/pedidos`
- Lista de pedidos que **tú has procesado**
- No verás pedidos de otros trabajadores (solo administradores pueden)

Información mostrada:
- Número de pedido
- Fecha y hora
- Total de la venta
- Estado actual
- Cliente (si aplica)

#### 5.2 Ver Detalle de Pedido
- **Ruta:** `/pedidos/<id>`
- Detalles completos del pedido:
  - Productos vendidos con cantidades
  - Precios unitarios y subtotales
  - Total del pedido
  - Método de pago utilizado
  - Estado actual
  - Información del cliente (si aplica)

#### 5.3 Actualizar Estado de Pedido
- **Ruta:** `/pedidos/<id_pedido>/actualizar` (POST)
- Cambiar el estado según el flujo de la venta

**Estados disponibles:**
1. **Pendiente:** Recién creado (estado inicial automático)
2. **Procesando:** En preparación para entrega
3. **Enviado:** En camino al cliente (si es envío)
4. **Entregado:** Completado exitosamente
5. **Cancelado:** Pedido cancelado (contacta al administrador)

**Flujo típico:**
```
Pendiente → Procesando → Enviado → Entregado
```

**Para ventas directas (en tienda):**
```
Pendiente → Procesando → Entregado
```

## Atajos y Navegación Rápida

| Función | Ruta | Atajo Dashboard |
|---------|------|-----------------|
| Inicio | `/` | Inicio |
| Dashboard Trabajador | `/dashboard` | - |
| Procesar Ventas | `/ventas` | Procesar Ventas |
| Productos | `/productos` | Gestionar Productos |
| Crear Producto | `/productos/crear` | - |
| Mis Pedidos | `/pedidos` | Ver Mis Pedidos |
| Inventario | `/productos` | Consultar Inventario |

---

**Versión:** 1.0  
**Última actualización:** Diciembre 2024  
**Sistema:** E-commerce con Gestión de Inventarios - Universidad Anáhuac Querétaro

## Recuerda

> "Tu rol como trabajador es fundamental para el éxito del negocio. Cada venta procesada correctamente, cada alerta de stock reportada a tiempo, y cada cliente atendido con excelencia contribuyen al crecimiento de la empresa. ¡Éxito en tu turno!"
