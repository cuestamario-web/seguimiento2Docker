from tabulate import tabulate

ACTIVIDADES = [
    ["Lunes", "8:00 AM", "Inauguración", "Auditorio principal"],
    ["Lunes", "10:00 AM", "Charla: Contenedores en la nube", "Sala 201"],
    ["Martes", "2:00 PM", "Taller de Docker", "Laboratorio 3"],
    ["Miércoles", "9:00 AM", "Hackathon", "Bloque C"],
    ["Jueves", "4:00 PM", "Panel de egresados", "Auditorio principal"],
    ["Viernes", "11:00 AM", "Premiación", "Auditorio principal"],
]


def mostrar(evento):
    print(f"AGENDA - {evento.upper()}")
    print(tabulate(ACTIVIDADES, headers=["Día", "Hora", "Actividad", "Lugar"],
                   tablefmt="rounded_grid"))
