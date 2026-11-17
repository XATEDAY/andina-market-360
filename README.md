# Andina Market 360

## Descripción
Proyecto académico que consolida y analiza las ventas ficticias de Lima, Ica y Arequipa para facilitar la toma de decisiones comerciales. Los resultados servirán como referencia para comparar el desempeño entre sedes.

## Problema empresarial
La empresa necesita consolidar sus ventas y consultar
los resultados por sede sin elaborar informes manualmente.

## Funcionalidades previstas
- Registrar 12 ventas ficticias.
- Calcular los totales de ventas por sede.
- Generar un resumen mediante Python.
- Ejecutar pruebas automáticas.
- Mostrar los resultados en una página web.

## Estructura del proyecto

- data/: archivos de ventas.
- src/: código fuente Python.
- tests/: pruebas automáticas.
- docs/: página web y resultados.
- .github/: automatizaciones de GitHub.

## Ejecución del análisis

Para ejecutar el análisis desde la terminal:

```bash
python src/resumen.py
```

## Estado del proyecto
Repositorio creado en GitHub.
La implementación del programa Python
y las pruebas están pendientes.

## Uso responsable
Se utilizarán datos ficticios.
No se almacenarán contraseñas ni credenciales.

## Reto 4.2 - Instrucciones de ejecución

### Problema identificado
El README inicial no explicaba completamente
los requisitos y pasos para ejecutar el proyecto.

### Requisitos
- Tener Python 3 instalado.
- Contar con Visual Studio Code o una terminal.
- Tener los archivos del proyecto disponibles.

### Procedimiento de ejecución

1. Abrir la carpeta andina-market-360.
2. Abrir una terminal en la raíz del proyecto.
3. Verificar que Python esté instalado:

```bash
python --version
```

4. Ejecutar el programa de análisis:

```bash
python src/resumen.py
```

5. Ejecutar las pruebas automáticas:

```bash
python -m unittest discover -s tests -v
```

### Resultado esperado
- Python debe mostrar su versión instalada.
- El programa debe procesar los registros de ventas.
- Las pruebas deben finalizar correctamente.

### Estado de comprobación
Las instrucciones están documentadas.
La ejecución del programa y las pruebas
está pendiente de implementar el código Python.

### Evidencia
CAP04_R02.png

## Capítulo 4 - Reto 4.3: Visibilidad del repositorio

### Objetivo
Analizar las diferencias entre un repositorio
privado y uno público en GitHub.

### Comparación

| Característica | Privado | Público |
|---|---|---|
| Acceso | Solo usuarios autorizados | Cualquier persona |
| Código fuente | Acceso restringido | Visible públicamente |
| Colaboración | Mediante permisos | Permite contribuciones públicas |
| Visibilidad | Limitada | Abierta |
| Uso | Proyectos internos | Proyectos abiertos o portafolios |

### Riesgos de cambiar a público

1. Exponer contraseñas o credenciales.
2. Publicar información confidencial.
3. Compartir archivos sin autorización.
4. Divulgar datos personales.
5. Exponer información sensible del historial de commits.

### Medidas preventivas

- Revisar los archivos antes de publicarlos.
- Verificar el funcionamiento de .gitignore.
- Revisar el historial de commits.
- Evitar incluir credenciales y datos reales.
- Comprobar las licencias y permisos de uso.

### Decisión

El repositorio XATEDAY/andina-market-360
permanecerá privado durante las prácticas.

Antes de hacerlo público se realizará una
revisión de seguridad y documentación.

### Resultado obtenido

Se identificaron las diferencias entre
repositorios públicos y privados, así como
los principales riesgos de publicación.

### Evidencia
CAP04_R03.png

## Propósito del proyecto

Andina Market 360 permite analizar las ventas ficticias de las sedes de Lima, Ica y Arequipa.

## Ejecución con Python

Para generar el resumen de ventas, utilizar el comando:

python src/resumen.py --json docs/data/resumen.json

## Resumen de ventas por sede

El informe mostrará los totales de ventas ficticias de Lima, Ica y Arequipa por separado para comparar los resultados de cada sede.

## Filtro de productos previsto

Al elegir un producto, el tablero deberá recalcular los totales por sede con las ventas de ese producto. La opción «Todos» deberá restaurar los totales generales.
