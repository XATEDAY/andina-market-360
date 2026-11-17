import unittest
from pathlib import Path

from src.resumen import DEFAULT_CSV, resumir


class ResumenVentasTests(unittest.TestCase):
    def test_total_general(self):
        self.assertEqual(resumir(DEFAULT_CSV)["total"], "1845.00")

    def test_totales_por_sede(self):
        self.assertEqual(
            resumir(DEFAULT_CSV)["sedes"],
            {"Lima": "814.00", "Ica": "555.00", "Arequipa": "476.00"},
        )

    def test_recuento_de_transacciones(self):
        self.assertEqual(resumir(DEFAULT_CSV)["operaciones"], 12)

    def test_totales_de_monitores(self):
        self.assertEqual(
            resumir(DEFAULT_CSV)["productos"]["Monitor"],
            {"Lima": "250.00", "Ica": "200.00", "Arequipa": "176.00"},
        )

    def test_calcula_desde_otro_csv(self):
        ruta = Path(__file__).with_name("fixtures") / "venta_decimal.csv"
        self.assertEqual(resumir(ruta)["total"], "0.30")
