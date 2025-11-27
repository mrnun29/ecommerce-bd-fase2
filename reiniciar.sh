#!/bin/bash
# Script para reiniciar el servidor Flask con Docker

echo "🔄 Reiniciando servidor Flask..."
docker restart ecommerce_web

echo "⏳ Esperando que el servidor inicie..."
sleep 5

# Verificar que el servidor esté funcionando
if curl -s -o /dev/null -w "%{http_code}" http://localhost:5001/ | grep -q "200"; then
    echo "✅ Servidor funcionando correctamente en http://localhost:5001"
else
    echo "❌ Error: El servidor no está respondiendo"
    echo "📋 Logs del contenedor:"
    docker logs ecommerce_web --tail 20
fi
