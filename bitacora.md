# Bitácora de cambios - Andina Market 360

## Capítulo 5 - Ejercicio 5.1

### Objetivo
Registrar una línea de base verificable
del proyecto y conservar una copia de seguridad.

### Versión inicial
- Versión: 1.0
- Fecha: 17/11/2026
- Archivo: data/ventas.csv
- Registros: 12 operaciones ficticias
- Total esperado: S/ 1,845.00

### Descripción
Se estableció la versión inicial del archivo
de ventas de Andina Market 360, con información
ficticia de las sedes Lima, Ica y Arequipa.

### Copia de seguridad
- Carpeta: Respaldo_Andina
- Archivo: ventas.csv
- Ubicación: Fuera del proyecto principal.

### Comprobación
Se utilizó PowerShell para contar los registros:

(Import-Csv .\data\ventas.csv).Count

Resultado obtenido: 12 registros.

La copia de seguridad permite recuperar
el archivo original si se modifica por error.

### Evidencia
CAP05_E01.png

## Capítulo 5 - Ejercicio 5.2

### Objetivo
Identificar los tres espacios de Git y comprender
cómo se registran los cambios de un proyecto.

### Los tres espacios de Git

1. Directorio de trabajo (Working Directory):
   Contiene los archivos que estamos modificando.

2. Área de preparación (Staging Area):
   Contiene los cambios seleccionados mediante
   el comando git add.

3. Historial (Repository):
   Almacena las versiones confirmadas mediante
   el comando git commit.

### Flujo de trabajo

[Directorio de trabajo]
         |
         | git add README.md
         v
[Área de preparación]
         |
         | git commit -m "Actualizar README"
         v
[Historial de versiones]

### Ejemplo práctico

Archivo utilizado: README.md

1. Se modifica el contenido del README.
2. Se utiliza git add para preparar los cambios.
3. Se utiliza git commit para registrar una versión.

### Comprobación
Modificar un archivo no genera automáticamente
un commit. Es necesario preparar y confirmar
los cambios mediante los comandos correspondientes.

### Resultado obtenido
Se identificaron los tres espacios de Git
y se representó el flujo para registrar versiones.

### Evidencia
CAP05_E02.png

## Capítulo 5 - Ejercicio 5.3

### Objetivo
Proponer un cambio controlado en la
documentación del proyecto.

### Archivo modificado
README.md

### Antes
Proyecto académico para analizar las ventas
ficticias de una empresa con sedes en Lima,
Ica y Arequipa.

### Después
Proyecto académico que consolida y analiza
las ventas ficticias de Lima, Ica y Arequipa
para facilitar la toma de decisiones comerciales.

### Motivo del cambio
Precisar el objetivo comercial del proyecto
y mejorar la claridad de su documentación.

### Mensaje de commit propuesto
docs: precisar objetivo comercial

### Comprobación
El cambio modifica únicamente la descripción
del proyecto en el README.md.

### Evidencia
CAP05_E03.png

## Capítulo 5 - Ejercicio 5.5

### Objetivo
Simular la recuperación de una versión anterior
de un archivo del proyecto.

### Archivo utilizado
README_copia.md

### Procedimiento
1. Se creó una copia del archivo README.md.
2. Se modificó el título de la copia.
3. Se comparó con el archivo original.
4. Se restauró el título original.

### Título modificado
# Andina Market 360 - VERSION MODIFICADA

### Título recuperado
# Andina Market 360

### Resultado obtenido
Se recuperó el título original del README,
corrigiendo la modificación realizada
durante la simulación.

### Comprobación
Se comparó el archivo restaurado con el
README original para verificar su contenido.

### Evidencia
CAP05_E05.png


## Capítulo 5 - Reto 5.1

### Objetivo
Identificar tres situaciones en las que Git
evita pérdidas de información y problemas
durante el trabajo colaborativo.

### Situación 1: Eliminación accidental

Problema:
Un desarrollador elimina por error una parte
importante del código del proyecto.

Solución:
Git permite recuperar el contenido desde
una versión anterior registrada.

### Situación 2: Cambios simultáneos

Problema:
Dos desarrolladores modifican el mismo
archivo y sus cambios generan conflictos.

Solución:
Git permite identificar los conflictos
y resolverlos antes de integrar los cambios.

### Situación 3: Confusión entre versiones

Problema:
El equipo tiene diferentes versiones de un
archivo y desconoce cuál es la más reciente.

Solución:
Git mantiene un historial de commits que
permite identificar los cambios realizados.

### Resultado obtenido
Se identificaron tres situaciones en las que
Git facilita la recuperación de información,
la colaboración y el seguimiento de versiones.

### Comprobación
Se relacionó cada problema con una función
específica del sistema de control de versiones.

### Evidencia
CAP05_R01.png


## Capítulo 5 - Reto 5.2

### Objetivo
Planificar cuatro cambios del proyecto
Andina Market 360 y establecer criterios
para comprobar su correcta implementación.

### Bitácora de cambios planificados

| N.º | Cambio planificado | Archivo | Criterio de aceptación |
|---|---|---|---|
| 1 | Mejorar la documentación | README.md | El objetivo y las instrucciones deben ser claros. |
| 2 | Validar registros de ventas | data/ventas.csv | Debe contener 12 operaciones ficticias. |
| 3 | Implementar el análisis de ventas | src/resumen.py | Debe calcular S/ 1,845.00 en ventas totales. |
| 4 | Implementar pruebas automáticas | tests/test_resumen.py | Deben aprobar cuatro pruebas. |

### Mensajes de commit propuestos

1. docs: mejorar documentacion
2. data: validar registros de ventas
3. feat: implementar resumen de ventas
4. test: agregar pruebas automaticas

### Resultado obtenido
Se planificaron cuatro cambios con sus
respectivos archivos y criterios de aceptación.

### Comprobación
Cada cambio cuenta con un resultado esperado
que podrá verificarse durante su implementación.

### Evidencia
CAP05_R02.png


## Capítulo 5 - Reto 5.3

### Objetivo
Explicar cuándo un archivo modificado todavía
no pertenece al historial de Git.

### Diagrama del proceso

[1. Directorio de trabajo]
    README.md modificado
            |
            | git add README.md
            v
[2. Área de preparación]
    Cambio preparado
            |
            | git commit -m "Actualizar README"
            v
[3. Historial de Git]
    Nueva versión registrada

### Explicación

1. Al modificar README.md, el cambio existe
   únicamente en el directorio de trabajo.

2. Al ejecutar git add, el cambio pasa al
   área de preparación, pero todavía no
   pertenece al historial de commits.

3. Al ejecutar git commit, Git registra
   una nueva versión en el historial.

### Resultado obtenido
Se representó el proceso de registro de cambios
y se identificó cuándo una modificación
todavía no pertenece al historial.

### Comprobación
Se determinó que los cambios solo forman
parte del historial después de confirmarlos
mediante git commit.

### Evidencia
CAP05_R03.png

## Control de salida del capítulo 5

| Verificación final | Estado |
|---|---|
| Realicé los cinco ejemplos y verifiqué los resultados. | Sí |
| Resolví los tres retos propuestos. | Sí |
| Guardé evidencias sin secretos ni datos reales. | Sí |
| Identifiqué una mejora para el capítulo siguiente. | Sí |

## Mejora para el siguiente capítulo

Configurar Git en el entorno local para comenzar
a registrar versiones reales del proyecto
Andina Market 360 mediante commits.

## Observaciones del estudiante

Se estudiaron los fundamentos del control
de versiones y los tres espacios de Git.

Se realizó una copia de seguridad del CSV,
se documentaron cambios y se simuló
la recuperación de un archivo.

Los ejercicios permitieron comprender
la importancia del historial de versiones.

La creación de commits reales queda
pendiente para el siguiente capítulo.
