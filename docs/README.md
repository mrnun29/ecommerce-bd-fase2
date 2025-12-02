# Documentación del Sistema de E-Commerce

Bienvenido a la documentación completa del Sistema de Comercio Electrónico con Gestión de Inventarios.

## Guías por Rol

Este sistema implementa un modelo de control de acceso basado en roles (RBAC). Cada rol tiene sus propias responsabilidades, permisos y flujos de trabajo.

### [Guía del Administrador](ADMINISTRADOR.md)

**Perfil:** Usuario con control total del sistema

**Contenido:**
- Descripción completa del rol y permisos
- Gestión de productos (CRUD completo)
- Administración de usuarios y trabajadores
- Gestión de proveedores y vinculación
- Panel de analíticas y reportes
- Control de inventario y alertas
- Gestión de pedidos del sistema
- APIs y endpoints disponibles
- Casos de uso detallados
- Solución de problemas comunes
- Mejores prácticas y recomendaciones

**Usuarios objetivo:** Administradores, gerentes, dueños del negocio

---

### [Guía del Trabajador](TRABAJADOR.md)

**Perfil:** Empleado encargado del punto de venta y operaciones diarias

**Contenido:**
- Descripción del rol y permisos
- Procesamiento de ventas (punto de venta)
- Gestión de productos básica
- Consulta y actualización de inventario
- Visualización y actualización de pedidos
- Procedimientos de turno (inicio, durante, fin)
- Casos de uso prácticos
- Checklists diarios, semanales y mensuales
- Tips para trabajadores
- Solución de problemas

**Usuarios objetivo:** Cajeros, vendedores, personal de piso de ventas

---

### [Guía del Proveedor](PROVEEDOR.md)

**Perfil:** Proveedor externo encargado de reabastecer inventario

**Contenido:**
- Descripción del rol y permisos limitados
- Consulta de inventario (solo lectura)
- Monitoreo de productos con stock bajo
- Registro de abastecimientos
- Historial de entregas y trazabilidad
- Vinculación con empresa proveedora
- Rutinas diarias y mensuales
- Generación de reportes para facturación
- Casos de uso de entregas
- Solución de problemas

**Usuarios objetivo:** Proveedores, distribuidores, representantes de ventas

---

## ¿Qué documentación leer?

### Si eres nuevo en el sistema:
1. Lee primero la [introducción del README principal](../README.md)
2. Revisa la sección de [Usuarios de Prueba](../README.md#-usuarios-de-prueba)
3. Abre la guía correspondiente a tu rol
4. Sigue las instrucciones de inicio de sesión

### Si buscas una función específica:
1. Usa el índice de contenidos al inicio de cada guía
2. Busca en la sección "Funcionalidades Principales"
3. Consulta "Casos de Uso Comunes" para ejemplos prácticos

### Si tienes un problema:
1. Revisa la sección "Solución de Problemas Comunes" de tu guía
2. Consulta las "Precauciones y Buenas Prácticas"
3. Si persiste, contacta al soporte (ver sección al final de cada guía)

## Estructura de las Guías

Cada guía sigue una estructura consistente:

```
1. Descripción del Rol
2. Credenciales de Acceso
3. Permisos y Capacidades
4. Funcionalidades Principales
   4.1 Dashboard
   4.2 Funciones específicas del rol
   4.3 Operaciones permitidas
5. Casos de Uso Comunes
6. Precauciones y Buenas Prácticas
7. Solución de Problemas Comunes
8. Estadísticas y Reportes
9. Navegación Rápida
10. Tips y Recomendaciones
11. Checklists
12. Contacto y Soporte
```

## Enlaces Rápidos

### Documentación General
- [README Principal](../README.md) - Información general del proyecto
- [Instalación](../README.md#-instalación-y-configuración) - Cómo instalar el sistema
- [Arquitectura](../README.md#️-arquitectura-del-sistema) - Estructura del proyecto

### Documentación Técnica
- [Base de Datos](../README.md#️-base-de-datos) - Esquema y tablas
- [Puntos Extra](PUNTOS_EXTRAS_IMPLEMENTADOS.txt) - Características avanzadas implementadas
- [Código Fuente](../app.py) - Aplicación principal

### Recursos
- [Repositorio GitHub](https://github.com/mrnun29/ecommerce-bd-fase2)
- [Modelos Python](../models/) - Lógica de negocio
- [Templates HTML](../templates/) - Interfaz de usuario

## Acceso al Sistema

**URL Local:** `http://localhost:5001`

**Credenciales de Prueba:**

| Rol | Correo | Contraseña | Guía |
|-----|--------|------------|------|
| Administrador | admin@ecommerce.com | admin123 | [Ver guía](ADMINISTRADOR.md) |
| Trabajador | trabajador@ecommerce.com | 123456 | [Ver guía](TRABAJADOR.md) |
| Proveedor | proveedor@ecommerce.com | 123456 | [Ver guía](PROVEEDOR.md) |

⚠️ **Importante:** Cambia las contraseñas por defecto en producción.

## Formación y Capacitación

### Nivel Básico (1-2 horas)
**Para:** Nuevos usuarios de cualquier rol
1. Leer sección "Descripción del Rol"
2. Practicar inicio de sesión
3. Explorar el dashboard
4. Realizar 1-2 casos de uso básicos

### Nivel Intermedio (3-5 horas)
**Para:** Usuarios que dominan lo básico
1. Completar todos los casos de uso comunes
2. Practicar con diferentes escenarios
3. Aprender atajos y navegación rápida
4. Familiarizarse con solución de problemas

### Nivel Avanzado (1 semana)
**Para:** Usuarios experimentados
1. Dominar todas las funcionalidades del rol
2. Optimizar flujos de trabajo
3. Implementar mejores prácticas
4. Capacitar a otros usuarios

## Soporte

**Documentación:**
- Consulta la guía específica de tu rol
- Revisa la sección de solución de problemas
- Verifica los casos de uso comunes

**Código y Técnico:**
- Issues en GitHub: [Reportar problema](https://github.com/mrnun29/ecommerce-bd-fase2/issues)
- Revisa el código en `models/` y `app.py`
- Consulta `schema_refactor.sql` para la estructura de BD

**Contacto:**
- Equipo de desarrollo (ver README principal)
- Administrador del sistema: admin@ecommerce.com

## Contribuciones a la Documentación

Si encuentras errores, mejoras o deseas agregar contenido:

1. Crea un issue en GitHub describiendo el cambio
2. Fork del repositorio
3. Realiza los cambios en la carpeta `docs/`
4. Envía un pull request con descripción detallada

**Guía de estilo:**
- Usa emojis para secciones principales
- Mantén el formato Markdown consistente
- Incluye ejemplos prácticos
- Sé claro y conciso
- Usa listas para mejor legibilidad

## Mejores Prácticas Generales

Independientemente de tu rol:

**Seguridad:**
- Nunca compartas tus credenciales
- Cierra sesión al terminar
- Cambia contraseñas periódicamente

**Operación:**
- Registra operaciones inmediatamente
- Verifica datos antes de confirmar
- Reporta problemas de inmediato

**Comunicación:**
- Mantén contacto con tu supervisor
- Documenta incidencias importantes
- Propón mejoras al sistema

**Aprendizaje:**
- Lee tu guía completa al menos una vez
- Practica en entorno de prueba
- Mantente actualizado con cambios

## Actualización de Documentación

**Versión actual:** 1.0  
**Última actualización:** Diciembre 2024  
**Sistema:** E-commerce con Gestión de Inventarios  
**Universidad:** Anáhuac Querétaro

**Historial de cambios:**
- v1.0 (Dic 2024): Documentación inicial completa por roles
  - Guía del Administrador (474 líneas)
  - Guía del Trabajador (532 líneas)
  - Guía del Proveedor (646 líneas)
  - README de documentación

---

## Comienza Ahora

1. **Identifica tu rol** en el sistema
2. **Abre tu guía:**
   - [Administrador](ADMINISTRADOR.md)
   - [Trabajador](TRABAJADOR.md)
   - [Proveedor](PROVEEDOR.md)
3. **Lee las primeras 3 secciones** (Descripción, Credenciales, Permisos)
4. **Inicia sesión** en `http://localhost:5001`
5. **Explora tu dashboard** y funcionalidades
6. **Practica con casos de uso** de la guía

¡Éxito en el uso del sistema! 

---

**Proyecto académico** - Universidad Anáhuac Querétaro © 2025  
**Curso:** Bases de Datos - Fase 2: Implementación  
**Equipo:** Alberto Romero, Diego Nuñez, Emilio Tolosa, Diego Vega
