# Proyecto integrador Andina Market 360

El equipo comercial necesita comparar las ventas por sede sin consolidarlas manualmente. La entrega procesa el CSV ficticio con Python, genera JSON y muestra tablas por sede y producto en un tablero estático.

## Alcance y aceptación

| Área | Responsable propuesto | Prioridad | Dependencia | Criterio |
|---|---|---|---|---|
| Datos | Custodia de datos | Alta | CSV ficticio | 12 transacciones y seis columnas |
| Procesamiento | Desarrollo | Alta | Datos | JSON reproducible y S/ 1845.00 según el CSV inicial |
| Pruebas | Calidad | Alta | Procesamiento | Unittest sin fallos |
| Web | Documentación | Media | JSON | Dos páginas enlazadas y filtro reversible |
| Seguridad | Mantenimiento | Alta | Repositorio | Sin secretos y CI con lectura de contenido |

Se asumen importes en soles y un archivo con encabezados válidos. Quedan fuera los datos de clientes, las ventas en vivo y el despliegue con costes. Los responsables son roles de trabajo pendientes de asignación grupal.

## Riesgos

| Riesgo | Control | Evidencia |
|---|---|---|
| Totales incorrectos | Aritmética decimal y pruebas por sede | [Pruebas](tests/test_resumen.py) |
| JSON desactualizado | Regeneración y comparación en CI | [Workflow](.github/workflows/pruebas.yml) |
| Enlaces rotos | Prueba HTTP de páginas y recursos | [Evidencia del capítulo 23](evidencia/cap23/INFORME_CAP23.md) |
| Secretos en informes | Canal privado y datos ficticios | [Política](SECURITY.md) |
| Integración sin validar | Revisión y pruebas previas | [Guía](CONTRIBUTING.md) |
