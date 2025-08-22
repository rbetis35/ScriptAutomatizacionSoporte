# Scripts de Automatización de Soporte (WIP)

Colección de utilidades en Python para tareas repetitivas de mesa de ayuda/soporte TI: lectura de logs, reportes rápidos y tareas programadas simples.

Este repositorio comenzará con un script para leer archivos `.log` y generar un CSV con el conteo de niveles (ERROR, WARN, INFO).

## Objetivos
- Acelerar análisis inicial de incidentes a partir de logs.
- Estandarizar salidas (CSV) para compartir con equipos N1/N2.
- Facilitar automatizaciones simples programables (cron/Task Scheduler).

## Estructura del proyecto
soporte-automation-scripts/
├─ parse_logs.py
├─ logs/ # Coloca aquí archivos .log (fuente)
├─ reportes/ # Salidas CSV de los reportes
└─ README.md


## Requisitos
- Python 3.9+ (recomendado)
- Sin dependencias externas para el script básico

## Uso rápido
1) Coloca uno o más archivos `.log` en la carpeta `logs/`.
2) Ejecuta:
python parse_logs.py

3) Se generará `reportes/errores_resumen.csv` con el conteo por nivel (ERROR, WARN, INFO).

Si no se encuentran logs `.log`, el script te avisará.

## Funcionalidades
- [x] Detección de niveles básicos en logs (ERROR, WARN, INFO) mediante regex
- [x] Conteo agregado y exportación a CSV
- [ ] Soporte para formatos de log comunes (Apache/Nginx/Systemd)
- [ ] Filtros por fecha/rango temporal
- [ ] Reporte HTML con gráficos simples
- [ ] Programación con cron/Task Scheduler (guías)
- [ ] Integración con email/Slack (enviar resumen)

## Configuración
- Directorios por defecto:
  - `LOG_DIR = logs`
  - `OUTPUT = reportes/errores_resumen.csv`
- Puedes editar estos valores en `parse_logs.py` según tu entorno.

## Buenas prácticas sugeridas
- Mantén archivos de ejemplo anonimizados en `logs/` para probar sin datos sensibles.
- Documenta brevemente el origen de cada log y su formato esperado.
- Evita subir información confidencial a repos públicos.

## Roadmap
- Parser por formato con autodetección.
- Conteo por servicio y por host.
- Exportaciones alternativas (XLSX, JSON) y envío por email.
- Dockerfile para ejecución programada en contenedor.

## Licencia
MIT (o la que prefieras)

## Estado
WIP — En desarrollo activo.
