# Guía de contribución

1. Acuerda el cambio con el equipo y registra su criterio de aceptación.
2. Actualiza tu copia con `git pull --ff-only origin main` desde un árbol limpio.
3. Crea una rama descriptiva para los cambios que requieran revisión.
4. Ejecuta `python -m unittest discover -s tests -v` y `git diff --check`.
5. En el Pull Request incluye las pruebas ejecutadas, sus resultados y la evidencia. Aplica las reglas vigentes de la rama.

Usa prefijos como `docs:`, `feat:` o `test:` en mensajes específicos. Reporta errores en Issues con pasos, resultado esperado, resultado observado y un CSV ficticio mínimo. Mantén fuera del repositorio datos reales, contraseñas y tokens.
