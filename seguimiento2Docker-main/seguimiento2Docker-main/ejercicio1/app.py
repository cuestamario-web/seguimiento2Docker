from evaluacion import cargar_notas, calcular_definitiva, estado


def main():
    estudiantes = cargar_notas("notas.csv")

    print("=" * 52)
    print("        REPORTE DE NOTAS - PROGRAMACION III")
    print("=" * 52)
    print(f"{'Estudiante':<22}{'Definitiva':>12}{'Estado':>16}")
    print("-" * 52)

    aprobados = 0
    for nombre, notas in estudiantes:
        definitiva = calcular_definitiva(notas)
        resultado = estado(definitiva)
        if resultado == "APROBADO":
            aprobados += 1
        print(f"{nombre:<22}{definitiva:>12.2f}{resultado:>16}")

    print("-" * 52)
    print(f"Aprobados: {aprobados} de {len(estudiantes)}")
    print("=" * 52)


if __name__ == "__main__":
    main()
