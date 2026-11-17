import argparse
import csv
import json
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

DEFAULT_CSV = Path(__file__).resolve().parents[1] / "data" / "ventas.csv"


def resumir(ruta):
    sedes = defaultdict(Decimal)
    productos = defaultdict(lambda: defaultdict(Decimal))
    operaciones = 0
    with Path(ruta).open(encoding="utf-8-sig", newline="") as archivo:
        for fila in csv.DictReader(archivo):
            importe = int(fila["cantidad"]) * Decimal(fila["precio_unitario"])
            sede, producto = fila["sede"], fila["producto"]
            sedes[sede] += importe
            productos[producto][sede] += importe
            operaciones += 1
    return {
        "operaciones": operaciones,
        "total": format(sum(sedes.values(), Decimal(0)), ".2f"),
        "sedes": {sede: format(total, ".2f") for sede, total in sedes.items()},
        "productos": {
            producto: {sede: format(total, ".2f") for sede, total in totales.items()}
            for producto, totales in sorted(productos.items())
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Resumen de ventas ficticias por sede")
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--json", type=Path, help="Ruta opcional del resumen JSON")
    args = parser.parse_args()
    salida = json.dumps(resumir(args.csv), ensure_ascii=False, indent=2) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(salida, encoding="utf-8")
    print(salida, end="")


if __name__ == "__main__":
    main()
