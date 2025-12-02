# Guía del Proveedor

## Descripción del Rol

El **Proveedor** es el rol encargado de monitorear el inventario y registrar abastecimientos de productos. Este rol tiene permisos limitados y especializados, enfocados en la gestión de suministro de mercancía.

## Credenciales de Acceso

- **Correo:** `proveedor@ecommerce.com`
- **Contraseña:** `123456`

**Importante:** Cambia tu contraseña después del primer inicio de sesión.

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

### ¿Qué hacer si no estoy vinculado?

1. Contacta al administrador del sistema
2. Proporciona:
   - Tu correo de acceso
   - Nombre de la empresa proveedora a la que perteneces
3. El administrador te vinculará a la empresa
4. Una vez vinculado, podrás registrar abastecimientos

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

## Casos de Uso Comunes

### Caso 1: Revisión Diaria de Stock Bajo

**Situación:** Comienzas tu jornada y quieres saber qué productos necesitan reabastecimiento.

**Pasos:**
1. Inicia sesión en el sistema
2. Ir a **Dashboard** → **Productos con Stock Bajo**
3. Revisar la lista completa
4. Anotar productos críticos (0-3 unidades)
5. Verificar tu inventario disponible
6. Planificar las entregas del día

**Frecuencia recomendada:** Diaria (al inicio de tu jornada)

### Caso 2: Entrega de Mercancía Programada

**Situación:** Llegas al almacén con una entrega de 50 laptops que estaban en stock bajo.

**Pasos:**
1. Descargar la mercancía físicamente
2. Iniciar sesión en el sistema
3. Ir a **Productos con Stock Bajo**
4. Localizar "Laptop Dell Inspiron 15"
5. Verificar el stock actual (ejemplo: 3 unidades)
6. En el campo "Cantidad", ingresar: **50**
7. Seleccionar tu empresa en el dropdown (si hay múltiples proveedores)
8. Clic en "Reabastecer"
9. Verificar la confirmación: "Producto reabastecido con 50 unidades"
10. Comprobar nuevo stock: 53 unidades

**Documentación recomendada:**
- Captura de pantalla de la confirmación
- Anotar el número de transacción (fecha y hora)
- Guardar para facturación

### Caso 3: Entrega de Múltiples Productos

**Situación:** Entregas varios productos en una sola visita.

**Pasos:**
1. Hacer una lista física de lo que entregas:
   ```
   - Laptop Dell: 50 unidades
   - Mouse Logitech: 100 unidades
   - Teclado RGB: 75 unidades
   ```

2. Para cada producto, repetir el proceso:
   - Ir a **Stock Bajo**
   - Buscar el producto
   - Ingresar cantidad
   - Reabastecer
   - Anotar confirmación

3. Al terminar, ir a **Mi Historial**
4. Verificar que todos los registros aparecen
5. Total de unidades debe coincidir con tu lista física

**Tip:** Haz los registros inmediatamente después de descargar cada producto.

### Caso 4: Verificar Historial para Facturación

**Situación:** Fin de mes, necesitas generar tu factura.

**Pasos:**
1. Ir a **Mi Historial**
2. Anotar todos los abastecimientos del mes:
   - Producto
   - Cantidad
   - Fecha
   - Precio unitario (para calcular total)
3. Calcular total de unidades entregadas
4. Calcular monto total a facturar
5. Generar factura según tu proceso interno
6. Enviar al departamento de pagos

**Ejemplo de cálculo:**
```
Laptop Dell (50 unidades × $12,999.00) = $649,950.00
Mouse Logitech (100 unidades × $399.00) = $39,900.00
Teclado RGB (75 unidades × $899.00) = $67,425.00
----------------------------------------
Total del mes: $757,275.00
```

### Caso 5: Planificación de Entregas Semanales

**Situación:** Quieres planificar tus entregas de la semana.

**Pasos:**
1. **Lunes:** Revisar stock bajo completo
2. Identificar productos críticos:
   - Stock 0-3: Prioridad alta (entregar hoy o mañana)
   - Stock 4-7: Prioridad media (entregar esta semana)
   - Stock 8-9: Prioridad baja (monitorear)
3. Verificar tu inventario disponible
4. Si no tienes existencias, hacer pedido a tu proveedor mayorista
5. Planificar rutas de entrega eficientes
6. **Durante la semana:** Hacer entregas según prioridades
7. **Viernes:** Revisar nuevamente stock bajo para la siguiente semana

### Caso 6: Responder a Alerta Urgente

**Situación:** El administrador te llama porque un producto se agotó.

**Pasos:**
1. Confirmar el producto específico
2. Verificar si tienes stock disponible
3. Si **tienes stock:**
   - Coordinar entrega inmediata
   - Registrar abastecimiento en el sistema
   - Notificar al administrador
4. Si **no tienes stock:**
   - Informar tiempo estimado de llegada
   - Hacer pedido urgente a tu proveedor mayorista
   - Mantener comunicación constante

**Tiempo de respuesta esperado:** 1-4 horas para productos críticos

## Precauciones y Buenas Prácticas

### Registro de Abastecimientos

**Registra inmediatamente después de la entrega**
- No esperes al final del día
- Mientras la mercancía está fresca en tu memoria
- Evita errores de cantidades

**Verifica las cantidades exactas**
- Cuenta físicamente la mercancía
- No registres "estimados"
- Si hay diferencias, anota y reporta

**Documenta cada entrega**
- Captura de pantalla de confirmación
- Anotación en tu bitácora personal
- Comprobante de entrega firmado (si aplica)

**Revisa el historial después de registrar**
- Confirma que el registro aparece
- Verifica que la cantidad sea correcta
- Asegúrate que la fecha y hora sean las esperadas

### Monitoreo de Inventario

**Revisa stock bajo diariamente**
- Establecer rutina (ejemplo: 8:00 AM)
- No esperar a que te llamen
- Ser proactivo en las entregas

**Comunica retrasos anticipadamente**
- Si no puedes cumplir una entrega, avisar con tiempo
- Proponer alternativas
- Mantener confianza con el cliente

**Planifica con anticipación**
- No esperar a que el stock llegue a 0
- Tener buffer de seguridad en tu inventario
- Coordinar con tu proveedor mayorista

### Seguridad

**Protege tus credenciales**
- No compartas tu usuario y contraseña
- Cambia la contraseña periódicamente
- Cierra sesión al terminar

**Solo registra entregas reales**
- Nunca registres abastecimientos que no hayas entregado
- Mantén la integridad del sistema
- Tu historial es tu reputación

**Verifica tu vinculación a la empresa**
- Si cambias de empresa, notifica al administrador
- Asegúrate que tu usuario esté vinculado correctamente

## Solución de Problemas Comunes

### Problema: No puedo registrar abastecimientos

**Posibles causas y soluciones:**

1. **No estás vinculado a una empresa proveedora**
   - **Solución:** Contacta al administrador
   - Proporciona tu correo y nombre de empresa
   - Espera a que te vinculen

2. **Error de permisos**
   - **Solución:** Verifica que tu rol sea "Proveedor"
   - Cierra sesión y vuelve a entrar
   - Si persiste, contacta al administrador

3. **Producto no encontrado**
   - **Solución:** Verifica el nombre exacto del producto
   - Busca en la lista de stock bajo
   - Si el producto no existe, notifica al administrador para que lo cree

### Problema: El stock no se actualizó después de mi abastecimiento

**Solución:**
1. Ve a **Mi Historial**
2. Verifica que el registro aparece
3. Anota la fecha y hora del registro
4. Ve a **Inventario** o **Stock Bajo**
5. Busca el producto
6. Refresca la página (F5)
7. Si el stock no cambió, contacta al administrador con:
   - Fecha y hora del abastecimiento
   - Producto
   - Cantidad registrada
   - Screenshot del historial

### Problema: No veo mi historial de abastecimientos

**Posibles causas:**

1. **No has registrado ningún abastecimiento aún**
   - El historial estará vacío hasta que registres el primero

2. **No estás vinculado a una empresa**
   - Contacta al administrador para vinculación

3. **Error de sesión**
   - Cierra sesión y vuelve a entrar
   - Limpia caché del navegador

### Problema: Registré una cantidad incorrecta

**Solución:**
1. **No puedes editar ni eliminar abastecimientos** (por seguridad y trazabilidad)
2. Contacta **inmediatamente** al administrador
3. Proporciona:
   - Fecha y hora del registro incorrecto
   - Producto
   - Cantidad registrada (incorrecta)
   - Cantidad real entregada (correcta)
4. El administrador puede:
   - Ajustar el stock manualmente
   - Registrar un ajuste de inventario
   - Actualizar el sistema

**Prevención:** Siempre verifica la cantidad antes de hacer clic en "Reabastecer"

### Problema: No aparezco como vinculado a mi empresa

**Solución:**
1. Ir a **Mi Historial**
2. Si no ves el nombre de una empresa, no estás vinculado
3. Contactar al administrador con:
   - Tu correo de acceso
   - Nombre completo de la empresa proveedora
   - RFC de la empresa (si aplica)
4. El administrador te vinculará
5. Cerrar sesión y volver a entrar
6. Verificar nuevamente en "Mi Historial"

## Estadísticas y Reportes

### Métricas Personales

Aunque no tienes acceso a analíticas completas, puedes calcular:

**Mensualmente:**
- Total de abastecimientos realizados
- Total de unidades entregadas
- Productos más abastecidos
- Monto total facturado

**Cálculo en Mi Historial:**
```
Ejemplo de reporte mensual (Noviembre 2024):

Total de abastecimientos: 25
Total de unidades: 2,150

Productos más abastecidos:
1. Mouse Logitech M170: 400 unidades
2. Laptop Dell Inspiron 15: 150 unidades
3. Teclado RGB: 300 unidades

Monto estimado: $1,500,000 MXN
```

### Exportar Datos (Manual)

Para generar reportes:
1. Ir a **Mi Historial**
2. Copiar información a Excel o Google Sheets
3. Calcular totales y subtotales
4. Generar gráficas si es necesario
5. Usar para facturación o análisis interno

## Atajos y Navegación Rápida

| Función | Ruta | Atajo Dashboard |
|---------|------|-----------------|
| Inicio | `/` | Inicio |
| Dashboard Proveedor | `/dashboard` | - |
| Inventario Completo | `/inventario` | Consultar Inventario |
| Stock Bajo | `/proveedores/stock-bajo` | Ver Stock Bajo |
| Registrar Abastecimiento | `/proveedores/reabastecer` | (desde Stock Bajo) |
| Mi Historial | `/proveedor/historial` | Mi Historial |

## Tips para Proveedores

### Rutina Diaria Recomendada

**8:00 AM - Revisión Matutina:**
1. Iniciar sesión
2. Consultar "Stock Bajo"
3. Identificar productos críticos (0-3 unidades)
4. Planificar entregas del día
5. Verificar inventario propio disponible

**Durante el Día - Entregas:**
1. Coordinar entregas según prioridades
2. Registrar cada abastecimiento inmediatamente
3. Verificar confirmación en el historial
4. Documentar con fotos/comprobantes

**5:00 PM - Cierre del Día:**
1. Revisar "Mi Historial" del día
2. Verificar que todos los registros estén correctos
3. Anotar totales de unidades entregadas
4. Actualizar tu inventario interno
5. Planificar entregas del día siguiente
6. Cerrar sesión

### Gestión Semanal

**Lunes:**
- Revisar stock bajo de toda la semana
- Planificar rutas de entrega eficientes
- Hacer pedidos a mayorista si es necesario

**Miércoles:**
- Punto de control: verificar progreso
- Ajustar plan si hay productos urgentes
- Confirmar entregas restantes

**Viernes:**
- Cerrar entregas de la semana
- Generar pre-reporte para facturación
- Anticipar necesidades de la siguiente semana

### Gestión Mensual

**Última semana del mes:**
- Generar reporte completo del mes
- Calcular totales para facturación
- Exportar historial si es necesario
- Enviar factura al departamento correspondiente
- Analizar productos más abastecidos
- Planificar inventario del siguiente mes

### Comunicación Efectiva

**Con el administrador:**
- Reporta problemas inmediatamente
- Propón mejoras en el proceso
- Mantén comunicación fluida

**Con tu proveedor mayorista:**
- Anticipa pedidos según tendencias
- Negocia tiempos de entrega
- Mantén stock de seguridad

**Documentación:**
- Lleva bitácora paralela (Excel o papel)
- Guarda comprobantes de entrega
- Mantén fotos de mercancía entregada

## Contacto y Soporte

**Para problemas técnicos del sistema:**
- Administrador: admin@ecommerce.com
- Soporte técnico: [teléfono/email]

**Para coordinación de entregas:**
- Administrador de inventario
- Gerente de operaciones

**Para dudas sobre facturación:**
- Departamento de cuentas por pagar
- Administración

## Checklist del Proveedor

### Diario
- [ ] Revisar stock bajo (8:00 AM)
- [ ] Planificar entregas del día
- [ ] Realizar entregas programadas
- [ ] Registrar cada abastecimiento en el sistema
- [ ] Verificar confirmaciones en el historial
- [ ] Documentar entregas
- [ ] Actualizar inventario propio
- [ ] Cerrar sesión

### Semanal
- [ ] Revisar tendencias de stock bajo
- [ ] Planificar rutas de entrega eficientes
- [ ] Hacer pedidos a proveedor mayorista
- [ ] Verificar comunicación con administrador
- [ ] Revisar historial semanal completo

### Mensual
- [ ] Generar reporte de abastecimientos del mes
- [ ] Calcular totales para facturación
- [ ] Enviar factura al departamento de pagos
- [ ] Analizar productos más abastecidos
- [ ] Planificar inventario del siguiente mes
- [ ] Proponer mejoras en el proceso

---

**Versión:** 1.0  
**Última actualización:** Diciembre 2024  
**Sistema:** E-commerce con Gestión de Inventarios - Universidad Anáhuac Querétaro

## Recuerda

> "Como proveedor, eres un eslabón fundamental en la cadena de suministro. Tu puntualidad, precisión en los registros y comunicación proactiva garantizan que el negocio nunca se quede sin inventario. ¡Tu trabajo es esencial para el éxito del comercio!"

## Ventajas del Sistema para Proveedores

- **Transparencia total:** Ves en tiempo real qué se necesita
- **Trazabilidad completa:** Historial detallado de todas tus entregas
- **Facturación simplificada:** Datos precisos para generar facturas
- **Comunicación eficiente:** Sistema centralizado, menos llamadas
- **Planificación mejorada:** Anticipas necesidades antes de que sean urgentes
- **Confianza del cliente:** Entregas documentadas y verificables
