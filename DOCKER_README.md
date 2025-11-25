# 🐳 Sistema de E-Commerce con Docker

## 🚀 Inicio Rápido

### Prerrequisitos
- Docker Desktop instalado y corriendo
- Git (opcional)

### Instalación y Ejecución

```bash
# 1. Ir al directorio del proyecto
cd /Users/diegomita/ecommerce_db

# 2. Construir y levantar los contenedores
docker-compose up --build

# 3. (Opcional) En otra terminal, insertar datos de prueba
docker-compose exec web python docker_seed.py
```

### Acceso
- **Aplicación Web:** http://localhost:5001
- **MySQL:** localhost:3306

### Credenciales

**Base de Datos:**
- Host: `localhost`
- Puerto: `3306`
- Usuario: `ecommerce_user`
- Contraseña: `ecommerce_pass`
- Base de datos: `ecommerce_db`

**Aplicación Web:**
- 👑 **Admin:** admin@ecommerce.com / admin123
- 👤 **Empleado:** empleado@ecommerce.com / empleado123
- 🛒 **Cliente:** cliente@email.com / cliente123

## 📋 Comandos Útiles

```bash
# Ver logs en tiempo real
docker-compose logs -f

# Ver solo logs de la aplicación
docker-compose logs -f web

# Ver solo logs de MySQL
docker-compose logs -f mysql

# Detener los contenedores
docker-compose down

# Detener y eliminar volúmenes (⚠️ elimina los datos)
docker-compose down -v

# Reiniciar solo la aplicación
docker-compose restart web

# Acceder a MySQL directamente
docker-compose exec mysql mysql -u ecommerce_user -pecommerce_pass ecommerce_db

# Ejecutar comandos en el contenedor web
docker-compose exec web python seed_data.py

# Ver estado de los contenedores
docker-compose ps
```

## 🔧 Troubleshooting

### El puerto 5001 está en uso
```bash
# Cambiar el puerto en docker-compose.yml:
ports:
  - "8080:5001"  # Usar puerto 8080 en tu máquina
```

### MySQL no inicia
```bash
# Ver logs detallados
docker-compose logs mysql

# Reiniciar MySQL
docker-compose restart mysql
```

### Resetear todo
```bash
# Eliminar todo y empezar de cero
docker-compose down -v
docker-compose up --build
```

## 📊 Estructura de Volúmenes

- `mysql_data`: Datos persistentes de MySQL
- `.:/app`: Código de la aplicación (montado en tiempo real)

## 🔄 Desarrollo

Los cambios en el código se reflejan automáticamente gracias al modo debug de Flask y al volumen montado.

Para aplicar cambios en dependencias:
```bash
docker-compose down
docker-compose up --build
```

## 🌐 Variables de Entorno

Puedes modificar las variables en `docker-compose.yml`:

```yaml
environment:
  DB_HOST: mysql
  DB_USER: ecommerce_user
  DB_PASSWORD: ecommerce_pass
  DB_NAME: ecommerce_db
  FLASK_ENV: development
```

## 🎯 Ventajas de usar Docker

✅ No necesitas instalar MySQL localmente  
✅ No hay problemas de contraseñas  
✅ Entorno consistente en cualquier máquina  
✅ Fácil de compartir con el equipo  
✅ Los datos persisten entre reinicios  
✅ Fácil de limpiar y resetear  

## 🆘 Soporte

Si tienes problemas:

1. Verifica que Docker Desktop esté corriendo
2. Revisa los logs: `docker-compose logs`
3. Asegúrate de que los puertos 5001 y 3306 estén libres
4. Intenta reiniciar: `docker-compose restart`
