# Proyecto Andina Market 360

## 1. Problema empresarial
Andina Market 360 es una empresa ficticia con sedes en Lima, Ica y Arequipa que necesita consolidar sus ventas y mostrar los resultados de cada sede sin elaborar informes manualmente.

## 2. Usuarios
Los usuarios principales serán los administradores y encargados de ventas de la empresa.

## 3. Resultado esperado
Desarrollar una solución que permita procesar los registros de ventas, calcular los totales por sede y presentar la información de manera organizada.

## 4. Preguntas comerciales
1. ¿Qué sede registra mayores ventas?
2. ¿Qué producto se vende más?
3. ¿Cómo cambia el total mensual de ventas?

## 5. Objetivo del proyecto
Automatizar el análisis de las ventas de Andina Market 360 para facilitar la consulta de información y apoyar la toma de decisiones.


## 6. Herramientas utilizadas

### Git
Es un sistema de control de versiones que permite registrar y conservar los cambios realizados en los archivos del proyecto de manera local.

### GitHub
Es una plataforma que permite alojar repositorios remotos, compartir proyectos y revisar los cambios realizados por otros colaboradores.

## 7. Flujo de trabajo

1. Archivo local: se crea o modifica un archivo del proyecto.
2. Git local: se registran los cambios realizados.
3. Repositorio remoto: los cambios se envían a GitHub.
4. Revisión del equipo: los colaboradores revisan los cambios antes de integrarlos.

Archivo local → Git local → GitHub → Revisión del equipo

## 8. Comprobación

GitHub no necesita ejecutar el programa de ventas para almacenar y revisar los cambios del proyecto. El procesamiento de ventas se realiza mediante Python.

## 9. Estructura del proyecto

El proyecto Andina Market 360 se organiza
de la siguiente manera:

andina-market-360/
├── proyecto.md
├── inventario.md
├── README.md
├── data/
│   └── ventas.csv
├── src/
│   └── resumen.py
├── tests/
│   └── test_resumen.py
├── docs/
│   ├── index.html
│   └── data/
│       └── resumen.json
└── .github/
    └── workflows/
        └── ci.yml

## 10. Justificación de la estructura

- data/: almacena los registros de ventas ficticias.
- src/: contiene el programa Python que procesa las ventas.
- tests/: permite verificar que los cálculos sean correctos.
- docs/: contiene la página web que muestra los resultados.
- .github/: almacena la configuración de colaboración y automatización.

## 11. Procesamiento de los datos

El archivo ventas.csv contiene los registros de ventas.

El programa resumen.py procesa estos datos
y genera el archivo resumen.json.

La página web utiliza el JSON generado para
mostrar los resultados sin modificar manualmente
el archivo CSV.

## 12. Estado de implementación

La estructura de carpetas ha sido creada.
Los archivos de procesamiento, pruebas y
visualización se incorporarán posteriormente.

## 13. Criterios de éxito

El proyecto Andina Market 360 tendrá los siguientes
objetivos medibles:

| Indicador | Meta | Responsable | Evidencia |
|---|---|---|---|
| Registro de ventas | Importar 12 ventas ficticias | Estudiante | ventas.csv |
| Análisis de ventas | Calcular totales por sede | Estudiante | resumen.json |
| Pruebas automáticas | Aprobar 4 pruebas | Estudiante | Resultado de terminal |
| Visualización web | Mostrar el resumen de ventas | Estudiante | Captura de la página web |

## 14. Comprobación

Cada objetivo podrá verificarse mediante archivos,
comandos o capturas de pantalla.

Los resultados se comprobarán cuando se implemente
y ejecute el proyecto.

## 15. Reto 1.1 - Nueva pregunta comercial

### Pregunta propuesta
¿Cuál es el promedio de ventas por operación
en cada sede de Andina Market 360?

### Archivo que produciría la respuesta
docs/data/resumen.json

### Procedimiento
El programa src/resumen.py procesará los regisstros
de data/ventas.csv para calcular el promedio
de ventas por operación en cada sede.

### Resultado esperado
Obtener el promedio de ventas correspondiente
a Lima, Ica y Arequipa.

### Comprobación
Verificar que los promedios se calculen correctamente
a partir de los registros del CSV.

## 16. Reto 1.2 - Roles del proyecto

### Objetivo
Definir tres roles y sus responsabilidades
para el desarrollo de Andina Market 360.

### Roles y responsabilidades

| Rol | Responsabilidad | Evidencia de revisión |
|---|---|---|
| Desarrollador | Implementar el código Python que procesa las ventas. | Código revisado |
| Tester | Ejecutar las pruebas y verificar los resultados. | Reporte de pruebas |
| Documentador | Mantener actualizado el README y la documentación. | Archivos Markdown revisados |

### Mapa de responsabilidades

Desarrollador
     ↓
Implementa el procesamiento de ventas
     ↓
Tester
     ↓
Comprueba el funcionamiento
     ↓
Documentador
     ↓
Registra los cambios y resultados

### Comprobación
Se definieron tres roles con responsabilidades
diferenciadas y evidencias de revisión previstas.

La ejecución y revisión real se realizarán
durante el desarrollo del proyecto.

## 17. Reto 1.3 - Clasificación de herramientas

### Objetivo
Clasificar cinco acciones del proyecto según
la herramienta que corresponde utilizar.

### Clasificación

| Acción | Herramienta | Justificación |
|---|---|---|
| Registrar cambios mediante commits | Git local | Guarda versiones del proyecto. |
| Consultar el historial de versiones | Git local | Permite revisar los commits anteriores. |
| Crear un Pull Request | GitHub | Permite solicitar la revisión de cambios. |
| Revisar un Issue | GitHub | Facilita el seguimiento de tareas y problemas. |
| Ejecutar el programa de ventas | Python | Procesa los datos del archivo CSV. |

### Resultado obtenido
Se clasificaron cinco acciones según su función:
dos pertenecen a Git local, dos a GitHub
y una a una herramienta externa.

### Comprobación
Se verificó que Git controla las versiones,
GitHub facilita la colaboración y Python
ejecuta el procesamiento de las ventas.

## 18. Control de salida del capítulo 1

| Verificación final | Estado |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos propuestos. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Pendiente de verificar |
| Identifiqué una mejora para el siguiente capítulo. | Sí |

## 19. Mejora para el capítulo siguiente

Preparar una cuenta profesional de GitHub
con medidas de seguridad adecuadas para
gestionar los repositorios del proyecto.

## 20. Observaciones del estudiante

Se desarrollaron los cinco ejemplos y los
tres retos correspondientes al capítulo 1.

Se definieron los objetivos, las herramientas,
la estructura del proyecto y las responsabilidades.

El proyecto base no fue proporcionado, por lo
que los archivos de código, datos y pruebas
se incorporarán posteriormente.



## Capítulo 4 - Ejercicio 4.5: Licencia del proyecto

### Objetivo
Evaluar una licencia adecuada para el proyecto
académico Andina Market 360.

### Estado del repositorio
- Nombre: andina-market-360
- Propietario: XATEDAY
- Visibilidad: Privado
- Uso: Académico

### Licencia evaluada
Licencia MIT.

### Características
- Permite utilizar, modificar y distribuir software.
- Permite el uso comercial.
- Exige conservar los avisos de copyright y licencia.
- No ofrece garantías sobre el funcionamiento del software.

### Decisión
El repositorio permanecerá privado durante
el desarrollo de las prácticas.

Se evaluará incorporar una licencia MIT
antes de publicar el proyecto, respetando
los derechos de autor y las condiciones
del material proporcionado por el docente.

### Comprobación
Se revisó la finalidad del proyecto y se
identificó una licencia de software conocida.

No se ha incorporado todavía un archivo LICENSE.

### Evidencia
CAP04_E05.png


## Capítulo 4 - Reto 4.1: Diseño de un repositorio

### Nombre del proyecto
TecnoStore

### Descripción
Tienda ficticia dedicada a la venta de productos
tecnológicos, como computadoras y accesorios.

### Objetivo
Diseñar un repositorio organizado para gestionar
productos, ventas y reportes de la tienda.

### Estructura propuesta

tecnostore/
├── README.md
├── data/
├── src/
├── tests/
├── docs/
└── config/

### Función de las carpetas

| Carpeta | Función |
|---|---|
| data/ | Almacenar productos y ventas. |
| src/ | Contener el código fuente. |
| tests/ | Guardar pruebas del sistema. |
| docs/ | Documentar el funcionamiento. |
| config/ | Almacenar configuraciones no sensibles. |

### Resultado obtenido
Se diseñó un repositorio para una tienda
tecnológica, definiendo cinco carpetas
con responsabilidades específicas.

### Comprobación
Se verificó que cada carpeta tiene una
función definida y que la estructura
permite organizar el desarrollo del proyecto.

### Evidencia
CAP04_R01.png


## Control de salida del capítulo 4

| Verificación final | Estado |
|---|---|
| Realicé los cinco ejemplos. | Sí |
| Resolví los tres retos propuestos. | Sí |
| Guardé las evidencias sin información sensible. | Sí |
| Identifiqué una mejora para el siguiente capítulo. | Sí |

## Mejoras pendientes

- Incorporar los archivos funcionales de Python.
- Implementar las pruebas automáticas.
- Verificar las instrucciones de ejecución del README.
- Comprobar el funcionamiento del archivo .gitignore.

## Mejora para el capítulo siguiente

Aplicar los fundamentos del control de versiones
para registrar los cambios del proyecto y
mantener un historial organizado.

## Observaciones del estudiante

Se creó el repositorio privado
XATEDAY/andina-market-360 en GitHub.

Se preparó la estructura local del proyecto,
la documentación README y el archivo .gitignore.

También se evaluaron las licencias y los riesgos
relacionados con la visibilidad del repositorio.

Los archivos todavía no se han sincronizado
con GitHub.
