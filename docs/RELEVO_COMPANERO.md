# Relevo para el siguiente integrante

## Acceso y rama de trabajo

El repositorio [XATEDAY/andina-market-360](https://github.com/XATEDAY/andina-market-360) es privado. Si aún no tienes acceso, el propietario debe invitarte como colaborador de GitHub. Acepta la invitación antes de clonar.

```bash
git clone https://github.com/XATEDAY/andina-market-360.git
cd andina-market-360
git switch main
git pull --ff-only origin main
git switch -c feature/mi-actividad
```

Si ya tienes un clon, empieza desde su directorio. Ejecuta `git status` y guarda tu trabajo pendiente antes de actualizar `main`. Usa un nombre de rama que describa tu actividad.

Realiza tus cambios en tu rama, revisa `git diff` y crea commits descriptivos. Publica tu rama con `git push -u origin feature/mi-actividad` y abre un Pull Request en GitHub con destino a `main`. Incluye el objetivo, la evidencia y el resultado real de las pruebas. Solicita revisión antes de fusionar. Un push forzado sobre la rama compartida puede apartar commits del equipo de su historial visible.

## Prácticas y archivos

| Capítulo | Trabajo registrado | Evidencias |
| --- | --- | --- |
| 8 | Resumen por sede, encabezado HTML, corrección del README, filtro documentado, gráficos de integración y comparación al cambiar de rama. | [Capítulo 8](../evidencia/cap8/) |
| 9 | Primera publicación en GitHub, edición web del README, comparación de fetch y pull en una copia y análisis del push forzado. | [Capítulo 9](../evidencia/cap9/) |
| 10 | Conflictos resueltos, revert, stash, reflog y consulta de commits anteriores en ramas locales de laboratorio. | [Capítulo 10](../evidencia/cap10/) |

Las imágenes PNG muestran la terminal real con las transcripciones originales o el resultado en GitHub. Los TXT contienen las salidas completas. Los sufijos numéricos indican páginas adicionales. Los commits de laboratorio se conservan en las ramas locales del repositorio de práctica y sus hashes se registran en las evidencias.

- [README.md](../README.md) describe el objetivo, la ejecución prevista y el filtro de productos.
- [docs/index.html](index.html) contiene el encabezado del tablero.
- [data/ventas.csv](../data/ventas.csv) contiene los datos ficticios de entrada.
- [src/resumen.py](../src/resumen.py) y [tests/test_resumen.py](../tests/test_resumen.py) están preparados como archivos iniciales.

## Continuidad

Continúa con el capítulo 11 del cuaderno. El cálculo de los totales por sede, sus pruebas y el filtro de productos quedan pendientes de implementación. La comprobación del capítulo 8 ejecutó `py -m unittest discover -s tests -v` y descubrió cero pruebas.
