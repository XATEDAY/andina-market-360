import csv
from collections import defaultdict


def cargar_ventas(ruta_archivo):
    ventas = []
    with open(ruta_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fila["cantidad"] = int(fila["cantidad"])
            fila["precio_unitario"] = float(fila["precio_unitario"])
            fila["total"] = fila["cantidad"] * fila["precio_unitario"]
            ventas.append(fila)
    return ventas


def resumen_por_sede(ventas):
    totales = defaultdict(float)
    for venta in ventas:
        totales[venta["sede"]] += venta["total"]
    return dict(totales)


def total_ventas(ventas):
    return sum(venta["total"] for venta in ventas)


def main():
    ventas = cargar_ventas("data/ventas.csv")
    totales = resumen_por_sede(ventas)
    total = total_ventas(ventas)
    print("Resumen de ventas por sede:")
    for sede, monto in totales.items():
        print(f"  {sede}: S/ {monto:.2f}")
    print(f"Total general: S/ {total:.2f}")


if __name__ == "__main__":
    main()
