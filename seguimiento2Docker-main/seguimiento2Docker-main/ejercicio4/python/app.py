import os
import platform

from tabulate import tabulate

# Pesos colombianos que vale 1 unidad de cada moneda (valores de ejemplo)
TASAS = {"USD": 4000.0, "EUR": 4400.0, "MXN": 220.0}

COMPRAS = {
    "Portatil": 2_800_000,
    "Celular": 1_150_000,
    "Audifonos": 180_000,
    "Silla ergonomica": 650_000,
}

moneda = os.environ.get("MONEDA_DESTINO", "USD")

if moneda not in TASAS:
    print(f"Moneda no soportada: {moneda}. Use USD, EUR o MXN.")
    raise SystemExit(1)

filas = [
    [producto, f"{precio:,.0f}", f"{precio / TASAS[moneda]:,.2f}"]
    for producto, precio in COMPRAS.items()
]

print(f"CONVERSOR DE MONEDAS (version Python {platform.python_version()})")
print(f"Moneda destino: {moneda}")
print(tabulate(filas, headers=["Producto", "Precio COP", f"Precio {moneda}"],
               tablefmt="grid", colalign=("left", "right", "right")))
