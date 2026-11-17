# Capítulo 3 - Ejercicio 3.2

## Examinar un repositorio público

### Repositorio seleccionado
- Nombre: BaaRai/ARTEX
- Plataforma: GitHub
- Visibilidad: Público
- URL: https://github.com/BaaRai/ARTEX

## Análisis de las secciones

| Sección | Función | Comparación con Andina Market 360 |
|---|---|---|
| Code | Permite consultar los archivos del proyecto. | Andina Market organizará sus archivos de ventas, código y documentación. |
| Issues | Permite registrar problemas y tareas. | Se utilizará para gestionar actividades pendientes. |
| Pull Requests | Permite proponer y revisar cambios. | Servirá para revisar modificaciones antes de integrarlas. |
| Actions | Permite ejecutar procesos automatizados. | Se utilizará para automatizar pruebas del proyecto. |
| Settings | Permite administrar la configuración del repositorio. | Se utilizará para configurar permisos y opciones del repositorio. |

## Comprobación

Se examinaron las secciones disponibles del
repositorio público ARTEX.

La sección Settings puede estar restringida
a los administradores del repositorio.

## Evidencia
CAP03_E02.png

## Ejercicio 3.3 - Buscar proyectos por tema

### Objetivo
Buscar y comparar dos repositorios públicos relacionados
con el análisis de ventas mediante Python.

### Repositorio 1
- Nombre: Python Data Analyzer
- Autor: ElenaHeydari
- URL: https://github.com/ElenaHeydari/python-data-analyzer
- Tecnologías: Python, Pandas, Streamlit y Decimal.

### Repositorio 2
- Nombre: Sales Revenue Dashboard
- Autor: Harshit06
- URL: https://github.com/Harshit06/sales-revenue-dashboard
- Tecnologías: Python, Pandas, Plotly y Streamlit.

### Matriz comparativa

| Criterio | Python Data Analyzer | Sales Revenue Dashboard |
|---|---|---|
| README | Claro y organizado | Más detallado y con índice |
| Documentación | Incluye instalación, ejecución y datos de entrada | Incluye instalación, arquitectura, gráficos y funcionalidades |
| Fuentes de datos | CSV | CSV, Excel y SQLite |
| Visualización | Dashboard con Streamlit | Dashboard con Streamlit y Plotly |
| Pruebas | Documenta pruebas con pytest | Incluye directorio tests; propone ampliar las pruebas |
| Historial | 3 commits observados | 4 commits observados |
| Mantenimiento | Continuidad no determinada | Continuidad no determinada |

### Conclusión
Ambos repositorios permiten analizar ventas mediante Python.

Python Data Analyzer destaca por su enfoque en
cálculos monetarios precisos y pruebas automatizadas.

Sales Revenue Dashboard presenta una documentación
más amplia y permite trabajar con diferentes
fuentes de datos y visualizaciones.

No se puede determinar cuál tiene mejor mantenimiento
únicamente por la cantidad de commits.

### Resultado obtenido
Se compararon dos repositorios públicos según
su documentación, funcionalidades e historial.

### Evidencia
CAP03_E03.png

## Ejercicio 3.4 - Seguimiento de un Issue

### Repositorio
streamlit/streamlit

### Issue seleccionado
- Número: #8351
- Título: File_uploader is not working
- Estado: Cerrado
- URL: https://github.com/streamlit/streamlit/issues/8351

### Cronología del problema

1. Problema:
   El 21/03/2024, un usuario reportó que el
   botón para subir archivos no funcionaba.

2. Debate:
   Un colaborador solicitó más detalles
   y sugirió revisar un problema similar.

3. Solución:
   El autor indicó que había probado las
   soluciones del problema relacionado.
   No especificó cuál resolvió el error.

4. Cierre:
   El Issue fue cerrado el 21/03/2024.

### Información que faltó
Habría sido útil incluir capturas del error,
pasos detallados para reproducirlo y confirmar
qué solución funcionó.

### Resultado obtenido
Se analizó la evolución de un problema real
desde su reporte hasta su cierre.

### Evidencia
CAP03_E04.png

## Ejercicio 3.5 - Historial de commits

### Repositorio analizado
- Nombre: Python Data Analyzer
- URL: https://github.com/ElenaHeydari/python-data-analyzer

### Historial de cambios

| Commit | Autor | Mensaje | Archivo modificado | Finalidad |
|---|---|---|---|---|
| 6a824ad | Saherwolfdi | Initial commit | analyzer.py, dashboard.py y otros | Crear la versión inicial del proyecto |
| ee74f7a | ElenaHeydari | Update project documentation | README.md | Mejorar la documentación |
| aa13f80 | ElenaHeydari | Updating | README.md | Actualizar el README |

### Análisis

- Versión inicial: se incorporaron los archivos
  necesarios para desarrollar el proyecto.
- Mejora: se actualizó la documentación del README.
- Corrección de errores: no se identificó un commit
  que indique claramente la solución de un error.

### Resultado obtenido
Se examinaron tres commits y se identificaron
sus autores, mensajes, archivos y finalidades.

### Evidencia
CAP03_E05.png

## Reto 3.1 - Mapa de navegación de GitHub

### Objetivo
Representar las principales secciones de GitHub
y explicar su utilidad en un proyecto.

### Mapa de navegación

GitHub
│
├── 1. Profile
│   └── Muestra la información del usuario.
│
└── 2. Repositories
    └── Permite consultar los repositorios.
        │
        ├── 3. Code
        │   └── Muestra los archivos del proyecto.
        │
        ├── 4. Issues
        │   └── Gestiona tareas y problemas.
        │
        ├── 5. Pull Requests
        │   └── Permite proponer y revisar cambios.
        │
        └── 6. Actions
            └── Automatiza pruebas y procesos.

### Resultado obtenido
Se elaboró un mapa de navegación con seis
secciones de GitHub y sus respectivas funciones.

### Comprobación
Se identificaron las secciones en la interfaz
de GitHub y se relacionaron con sus utilidades
para el proyecto Andina Market 360.

### Evidencia
CAP03_R01.png

## Reto 3.2 - Comparación de repositorios públicos

### Repositorios analizados

1. Python Data Analyzer
   https://github.com/ElenaHeydari/python-data-analyzer

2. Sales Revenue Dashboard
   https://github.com/Harshit06/sales-revenue-dashboard

### Matriz comparativa

| Criterio | Python Data Analyzer | Sales Revenue Dashboard |
|---|---|---|
| README | Claro, organizado y con instrucciones de instalación | Detallado, con índice y ejemplos visuales |
| Licencia | No se encontró archivo LICENSE en la raíz | Licencia MIT |
| Historial | 3 commits | 4 commits |
| Último commit | 29/10/2026 | 13/07/2026 |
| Documentación | Explica el procesamiento y las pruebas | Explica funcionalidades y arquitectura |

### Análisis

Python Data Analyzer tiene documentación clara
y registra cambios más recientes.

Sales Revenue Dashboard presenta documentación
más extensa y cuenta con una licencia MIT.

La cantidad de commits no es suficiente para
determinar la calidad del mantenimiento.

### Resultado obtenido
Se compararon dos repositorios públicos
considerando su README, licencia e historial.

### Evidencia
CAP03_R02.png

## Reto 3.3 - Ficha de un Issue público

### Identificación
- Repositorio: streamlit/streamlit
- Issue: #8351
- Título: File_uploader is not working
- Tipo: Bug
- Estado: Cerrado
- Fecha: 21/03/2024
- URL: https://github.com/streamlit/streamlit/issues/8351

### Problema reportado
El usuario informó que el componente
st.file_uploader dejó de funcionar después
de actualizar Streamlit.

### Pasos observados
1. El usuario reportó el problema.
2. Un colaborador solicitó más información.
3. Se compartió una referencia a un problema similar.
4. El usuario probó las soluciones sugeridas.
5. El Issue fue cerrado como completado.

### Evidencias
- Descripción del error.
- Versión de Streamlit: 1.32.2.
- Versión de Python: 3.9.
- Comentarios de los participantes.
- Estado final: Closed.

### Resultado obtenido
Se documentó un Issue público, identificando
el problema, su seguimiento y estado final.

### Comprobación
Se verificó el historial de comentarios
y el cierre del Issue en GitHub.

No se especificó qué solución exacta
resolvió el problema.

### Evidencia
CAP03_R03.png

## Control de salida del capítulo 3

| Verificación final | Estado |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos propuestos. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

## Mejora para el siguiente capítulo

Crear y organizar el repositorio Andina Market 360
en GitHub, incorporando una estructura de archivos
adecuada y documentación clara.

## Observaciones del estudiante

Se exploró la interfaz de GitHub y se analizaron
repositorios públicos, historiales de commits
e Issues.

También se compararon proyectos de Python y
se identificaron las principales herramientas
de colaboración disponibles en GitHub.
