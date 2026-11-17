# Manual de operación

Genera el resumen desde la raíz con `python src/resumen.py --json docs/data/resumen.json`. Abre el [tablero](index.html) desde el servidor local descrito en el [README](../README.md). Selecciona un producto para comparar sedes y vuelve a **Todos** para recuperar el resumen general.

| Indicador | Cálculo | Fuente |
|---|---|---|
| Operaciones | Filas de venta | [CSV](../data/ventas.csv) |
| Venta total en soles | Suma de cantidad por precio unitario | [CSV](../data/ventas.csv) |
| Venta por sede | Agrupación del importe por sede | [CSV](../data/ventas.csv) |
| Venta por producto y sede | Agrupación del importe por producto y sede | [CSV](../data/ventas.csv) |

Python genera el JSON antes de la publicación. El navegador descarga el JSON por HTTP. Ante un error de carga, comprueba que la generación terminó y que el servidor apunta a `docs`.

## Indicadores por sede

El script calcula automáticamente los importes de las tres sedes.

| Sede | Indicador | Fórmula | Fuente |
|---|---|---|---|
| Lima | Ventas en soles | Suma de cantidad × precio por sede | [CSV](../data/ventas.csv) |
| Ica | Ventas en soles | Suma de cantidad × precio por sede | [CSV](../data/ventas.csv) |
| Arequipa | Ventas en soles | Suma de cantidad × precio por sede | [CSV](../data/ventas.csv) |
