# Guía del Trabajador

## Descripción del Rol

El **Trabajador** (o Empleado) es el rol encargado de procesar ventas directas en el punto de venta, gestionar el inventario y atender las operaciones diarias del comercio. Este rol tiene permisos intermedios enfocados en las operaciones de venta.

## Credenciales de Acceso

- **Correo:** `trabajador@ecommerce.com`
- **Contraseña:** `123456`

**Importante:** Cambia tu contraseña después del primer inicio de sesión.

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

## Casos de Uso Comunes

### Caso 1: Venta Rápida en Mostrador

**Situación:** Un cliente llega y quiere comprar 1 laptop y 1 mouse.

**Pasos:**
1. Ir a **Dashboard** → **Procesar Ventas**
2. Seleccionar "Laptop Dell Inspiron 15" (cantidad: 1)
3. Clic en "+" para agregar otro producto
4. Seleccionar "Mouse Logitech M170" (cantidad: 1)
5. Seleccionar método de pago: "Efectivo"
6. Clic en "Procesar Venta"
7. Verificar el número de pedido generado
8. Entregar productos al cliente

**Tiempo estimado:** 1-2 minutos

### Caso 2: Venta con Múltiples Productos

**Situación:** Cliente compra varios artículos para su oficina.

**Pasos:**
1. Acceder a **Procesar Ventas**
2. Ir agregando productos uno por uno:
   - Laptop (cantidad: 3)
   - Mouse (cantidad: 3)
   - Teclado (cantidad: 3)
   - Monitor (cantidad: 2)
3. Verificar el total calculado automáticamente
4. Seleccionar método de pago: "Transferencia"
5. Procesar la venta
6. Imprimir o mostrar comprobante al cliente

### Caso 3: Alertar sobre Stock Bajo

**Situación:** Notas que un producto popular está por agotarse.

**Pasos:**
1. Ir a **Productos**
2. Identificar productos en rojo (stock bajo)
3. Anotar el nombre y código del producto
4. Notificar al administrador o proveedor:
   - Vía correo electrónico
   - Llamada telefónica
   - Sistema de tickets (si existe)
5. Registrar la alerta en un documento interno

**Productos a monitorear:**
- Artículos de alta rotación
- Productos en promoción
- Temporada alta

### Caso 4: Corrección de Stock después de Inventario

**Situación:** Realizaste un conteo físico y encontraste diferencias.

**Pasos:**
1. Ir a **Productos** → **Editar Producto**
2. Localizar el producto con discrepancia
3. Actualizar el campo "Stock" con la cantidad física real
4. Guardar cambios
5. Documentar la diferencia en un reporte interno
6. Notificar al administrador si la diferencia es significativa

**Ejemplo:**
```
Producto: Mouse Logitech M170
Stock en sistema: 45
Stock físico: 42
Acción: Actualizar stock a 42
Diferencia: -3 unidades (posible merma o error previo)
```

### Caso 5: Actualizar Estado de Pedidos

**Situación:** Procesaste ventas en la mañana y ahora las entregas están completas.

**Pasos:**
1. Ir a **Mis Pedidos**
2. Identificar pedidos en estado "Procesando"
3. Para cada pedido entregado:
   - Clic en el pedido
   - Seleccionar nuevo estado: "Entregado"
   - Confirmar cambio
4. Los pedidos ahora muestran "Entregado"

### Caso 6: Agregar Producto Nuevo al Catálogo

**Situación:** Llegó mercancía nueva que no está en el sistema.

**Pasos:**
1. Ir a **Productos** → **Crear Producto**
2. Llenar formulario con la información de la caja/etiqueta:
   - Nombre del producto
   - Descripción completa
   - Precio de venta sugerido
   - Cantidad recibida (stock inicial)
   - Nivel mínimo (consultar con administrador o usar 10)
3. Guardar
4. Verificar que el producto aparece en el catálogo
5. Ya está disponible para vender

## Precauciones y Buenas Prácticas

### Durante las Ventas

**Verificar stock antes de confirmar**
- Siempre revisa que haya stock disponible antes de prometer al cliente
- El sistema validará automáticamente, pero es mejor prevenir

**Confirmar método de pago**
- Pregunta al cliente cómo pagará antes de procesar
- Para Efectivo: verifica que tengas cambio
- Para Tarjeta: asegúrate de tener terminal disponible
- Para Transferencia: proporciona datos bancarios correctos

**Revisar el total antes de procesar**
- Verifica que las cantidades sean correctas
- Confirma que el precio mostrado sea el actual
- Si hay dudas, consulta con el administrador

**Entregar comprobante**
- Siempre proporciona el número de pedido al cliente
- Si es posible, imprime o envía comprobante digital

### Gestión de Inventario

**Reportar stock bajo inmediatamente**
- No esperes a que se agote completamente
- Notifica cuando llegue al nivel mínimo

**Actualizar stock solo con certeza**
- No hagas ajustes "por estimación"
- Solo actualiza después de conteo físico

**Documentar discrepancias**
- Si encuentras diferencias, anótalas
- Reporta al administrador para investigación

### Seguridad

**Mantén tus credenciales seguras**
- No compartas tu usuario y contraseña
- Cierra sesión al terminar tu turno

**Verifica identidad en pagos con tarjeta**
- Solicita identificación si es necesario
- Valida firma en el voucher

**No proceses ventas sin autorización**
- Solo ventas reales y autorizadas
- No hagas ventas "de favor" sin pago

## Solución de Problemas Comunes

### Problema: No puedo procesar una venta

**Posibles causas y soluciones:**

1. **Stock insuficiente**
   - Verifica el stock disponible del producto
   - Reduce la cantidad solicitada
   - Consulta con el administrador sobre reabastecimiento

2. **Producto no encontrado**
   - Busca el producto en el catálogo
   - Si no existe, créalo (con permiso del administrador)

3. **Error en el sistema**
   - Refresca la página
   - Cierra sesión y vuelve a entrar
   - Contacta soporte técnico

### Problema: El stock no se actualizó después de una venta

**Solución:**
1. Verifica el estado del pedido (no debe estar en "Cancelado")
2. Consulta el detalle del pedido para confirmar que se procesó
3. Refresca la página de productos
4. Si persiste, contacta al administrador

### Problema: No veo todos los pedidos

**Aclaración:** Como trabajador, solo ves los pedidos que **tú procesaste**. Esto es normal. Solo el administrador ve todos los pedidos del sistema.

### Problema: No puedo editar un producto

**Posibles causas:**
1. **Permisos insuficientes:** Verifica tu rol (debe ser Trabajador)
2. **Producto en uso:** Puede estar en un pedido activo
3. **Error del sistema:** Contacta al administrador

### Problema: Procesé una venta incorrecta

**Solución:**
1. No intentes eliminar el pedido (no tienes permisos)
2. Contacta inmediatamente al administrador
3. Proporciona el número de pedido
4. El administrador puede cambiar el estado a "Cancelado"
5. Procesa una nueva venta con los datos correctos

## Estadísticas y Reportes

Aunque no tienes acceso al panel completo de analíticas (solo para administradores), puedes:

- Ver tus propios pedidos procesados
- Consultar el historial de ventas que realizaste
- Verificar el total de ventas por día (sumando tus pedidos)
- Identificar productos más vendidos por ti

**Reporte Manual Diario:**
1. Ir a **Mis Pedidos**
2. Filtrar por fecha de hoy
3. Anotar:
   - Número de ventas realizadas
   - Total de ingresos generados
   - Productos más vendidos
4. Reportar al administrador o supervisor

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

## Tips para Trabajadores

### Inicio de Turno
1. Inicia sesión con tus credenciales
2. Verifica que el sistema esté funcionando correctamente
3. Consulta productos con stock bajo
4. Prepara terminal de pago y caja
5. Revisa si hay pedidos pendientes de entregas

### Durante el Turno
1. Procesa ventas con precisión y rapidez
2. Mantén organizada la caja
3. Actualiza estados de pedidos conforme avances
4. Reporta anomalías inmediatamente
5. Atiende alertas de stock bajo

### Fin de Turno
1. Verifica que todos los pedidos del día tengan estado correcto
2. Haz corte de caja (procedimiento interno)
3. Reporta ventas totales al supervisor
4. Nota productos que necesitan reabastecimiento
5. Cierra sesión correctamente

### Atención al Cliente
1. Saluda amablemente
2. Confirma disponibilidad antes de prometer
3. Explica métodos de pago disponibles
4. Proporciona comprobante siempre
5. Agradece por la compra

## Soporte y Contacto

**Para problemas técnicos:**
- Contacta al administrador del sistema
- Correo: admin@ecommerce.com
- Teléfono interno: [número interno]

**Para dudas de productos o precios:**
- Consulta con tu supervisor
- Revisa catálogo de productos
- Contacta al proveedor (si aplica)

**Para reportar incidencias:**
- Documento interno de incidencias
- Sistema de tickets (si aplica)
- Llamada directa al administrador

## Checklist del Trabajador

### Diario
- [ ] Iniciar sesión al comenzar turno
- [ ] Verificar productos con stock bajo
- [ ] Procesar ventas del día
- [ ] Actualizar estados de pedidos
- [ ] Hacer corte de caja
- [ ] Reportar ventas totales
- [ ] Cerrar sesión al terminar

### Semanal
- [ ] Revisar historial de ventas de la semana
- [ ] Reportar productos de alta rotación
- [ ] Verificar que no haya pedidos pendientes antiguos
- [ ] Notificar productos que requieren reabastecimiento urgente

### Mensual
- [ ] Participar en inventario físico
- [ ] Revisar desempeño personal de ventas
- [ ] Sugerir mejoras en el proceso de venta
- [ ] Actualizar conocimiento de productos nuevos

---

**Versión:** 1.0  
**Última actualización:** Diciembre 2024  
**Sistema:** E-commerce con Gestión de Inventarios - Universidad Anáhuac Querétaro

## Recuerda

> "Tu rol como trabajador es fundamental para el éxito del negocio. Cada venta procesada correctamente, cada alerta de stock reportada a tiempo, y cada cliente atendido con excelencia contribuyen al crecimiento de la empresa. ¡Éxito en tu turno!"
