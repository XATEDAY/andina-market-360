# bug: cifra incorrecta tras editar CSV

Caso de laboratorio: una copia del CSV cambia la cantidad de V001 de 1 a 2. Si se sirve el JSON anterior, Lima sigue mostrando S/ 814,00 cuando debería mostrar S/ 1.064,00 y el total general debería subir a S/ 2.095,00. Regenerar el resumen de la copia soluciona el desfase.

Criterio: tras corregir los datos publicados, el JSON debe coincidir con el cálculo independiente. Etiquetas propuestas: error y prioridad-alta.
