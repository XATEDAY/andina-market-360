# Bitácora de Integración Continua (CI) — Andina Market 360

## Registro de Ejecuciones

| Entorno | Evento | Commit | Job | Resultado | Causa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub Actions (Remoto)** | `push` (`practica/cap21-actions`) | `148f520` | `pruebas-unitarias` | Aprobado (Verde) | Ejecución exitosa de `python -m unittest discover -s tests` (`Ran 1 test ... OK`) en el runner `ubuntu-latest`. |
| **Entorno Local (Windows)** | Ejecución manual en terminal | `148f520` | N/A (Local) | No ejecutado / Simulado | El equipo local no cuenta con el intérprete de Python instalado (`CommandNotFoundException`), por lo que la validación real se delegó al runner remoto de GitHub Actions. |

## Diferencia entre ejecución local y ejecución en GitHub Actions
* **Ejecución local:** Depende de la configuración de la máquina del desarrollador (sistema operativo, versión de Python instalada y variables de entorno). Sirve para validar cambios antes de hacer commit.
* **Ejecución en GitHub Actions:** Se ejecuta en un contenedor limpio y reproducible (`ubuntu-latest`) disparado automáticamente por eventos de Git (`push` o `pull_request`), garantizando que las pruebas corran siempre bajo las mismas condiciones para todo el equipo.

## Protocolo de acción si el job aparece en rojo
1. Abrir la pestaña **Actions** en GitHub, ingresar al job fallido y revisar el log del paso con error (identificar la línea exacta y el tipo de fallo, como `AssertionError` o `SyntaxError`).
2. Reproducir el fallo en el entorno local corriendo `python -m unittest discover -s tests`.
3. Corregir el código fuente o la prueba unitaria afectada.
4. Confirmar el cambio con un nuevo `commit` y realizar `push` a la rama para verificar que el workflow vuelva a estado **verde** antes de aprobar un Pull Request.