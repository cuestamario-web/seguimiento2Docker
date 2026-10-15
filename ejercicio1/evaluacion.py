import csv
import os

# Porcentajes de cada corte (deben sumar 1.0)
PESO_CORTE_1 = 0.30
PESO_CORTE_2 = 0.30
PESO_CORTE_3 = 0.40

ESCALA_MAXIMA = 5.0
MINIMA_PARA_APROBAR = float(os.getenv("NOTA_APROBACION", "3.0"))


def cargar_notas(ruta):
    estudiantes = []
    with open(ruta, encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            notas = [float(fila["corte1"]), float(fila["corte2"]), float(fila["corte3"])]
            estudiantes.append((fila["nombre"], notas))
    return estudiantes


def calcular_definitiva(notas):
    c1, c2, c3 = notas
    definitiva = c1 * PESO_CORTE_1 + c2 * PESO_CORTE_2 + c3 * PESO_CORTE_3
    return min(definitiva, ESCALA_MAXIMA)


def estado(definitiva):
    return "APROBADO" if definitiva >= MINIMA_PARA_APROBAR else "REPROBADO"
