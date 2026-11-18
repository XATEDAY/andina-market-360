# Capítulo 21 · Introducción a GitHub Actions

Cuaderno, páginas 44–45.

Caso que continúa: Automatizar las pruebas del caso mediante un workflow reproducible.
Meta práctica: completar cinco ejemplos resueltos y tres ejercicios propuestos, conservar evidencias y dejar listo el proyecto
para el capítulo 22.

Comandos / rutas de consulta del capítulo:
name: Pruebas
on: [push, pull_request]
permissions: {contents: read}

## Actividades

- [CAP21_E01 · Inspeccionar un archivo YAML](ejemplos/E01/resultado.md)
- [CAP21_E02 · Activar una ejecución por push](ejemplos/E02/resultado.md)
- [CAP21_E03 · Usar un runner sin privilegios innecesarios](ejemplos/E03/resultado.md)
- [CAP21_E04 · Provocar y estudiar una ejecución](ejemplos/E04/resultado.md)
- [CAP21_E05 · Explicar un resultado al equipo](ejemplos/E05/resultado.md)
- [CAP21_R01 · Escriba un workflow mínimo para ejecutar las pruebas del caso ante cada Pull Request.](retos/R01/resultado.md)
- [CAP21_R02 · Explique tres fallos que no se solucionan aumentando permisos del workflow.](retos/R02/resultado.md)
- [CAP21_R03 · Elabore una ficha de diagnóstico de un job que no aparece en Actions.](retos/R03/resultado.md)

[Control de salida](CONTROL_CAP21.md)
