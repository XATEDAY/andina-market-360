# Capítulo 20 · Gestión de archivos y paquetes

Cuaderno, páginas 42–43.

Caso que continúa: Controlar el tamaño del repositorio y preparar archivos distribuibles del dashboard.
Meta práctica: completar cinco ejemplos resueltos y tres ejercicios propuestos, conservar evidencias y dejar listo el proyecto
para el capítulo 21.

Comandos / rutas de consulta del capítulo:
git check-ignore -v dist/prueba.tmp
git lfs version   # Solo si Git LFS está instalado

## Actividades

- [CAP20_E01 · Auditar archivos pesados](ejemplos/E01/resultado.md)
- [CAP20_E02 · Ampliar reglas de exclusión](ejemplos/E02/resultado.md)
- [CAP20_E03 · Simular un caso para Git LFS](ejemplos/E03/resultado.md)
- [CAP20_E04 · Empaquetar una versión local](ejemplos/E04/resultado.md)
- [CAP20_E05 · Diseñar un paquete reutilizable](ejemplos/E05/resultado.md)
- [CAP20_R01 · Elabore una política de archivos permitidos y prohibidos en Git.](retos/R01/resultado.md)
- [CAP20_R02 · Empaquete la versión del dashboard y registre su contenido y tamaño.](retos/R02/resultado.md)
- [CAP20_R03 · Proponga metadatos mínimos para distribuir una librería propia del caso.](retos/R03/resultado.md)

[Control de salida](CONTROL_CAP20.md)

## Ejecución registrada

- [CAP20_E01](ejemplos/E01/resultado.md) · COMPLETADO Y VERIFICADO. Cinco tamaños medidos en data y docs.
- [CAP20_E02](ejemplos/E02/resultado.md) · COMPLETADO Y VERIFICADO. Git no lista dist/prueba.tmp y muestra la regla dist/.
- [CAP20_E03](ejemplos/E03/resultado.md) · COMPLETADO Y VERIFICADO. Archivos hipotéticos y cliente cotejado sin activar LFS.
- [CAP20_E04](ejemplos/E04/resultado.md) · COMPLETADO Y VERIFICADO. ZIP extraído y comparado.
- [CAP20_E05](ejemplos/E05/resultado.md) · COMPLETADO Y VERIFICADO. Nombre, versión, API, estructura e instalación prevista.
- [CAP20_R01](retos/R01/resultado.md) · COMPLETADO Y VERIFICADO. Clases permitidas y prohibidas con criterio.
- [CAP20_R02](retos/R02/resultado.md) · COMPLETADO Y VERIFICADO. Tamaño, SHA-256, seis miembros y extracción correctos.
- [CAP20_R03](retos/R03/resultado.md) · COMPLETADO Y VERIFICADO. Versión, Python, dependencia, licencia pendiente y API documentados.

## Capturas del corte

8 PNG enlazados en las fichas y la matriz. Las capturas de documentos y transcripciones muestran los artefactos locales abiertos en Chrome.
