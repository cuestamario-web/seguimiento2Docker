import importlib
import os

# Cada perfil ejecuta un módulo distinto de la carpeta "salidas"
# y cada módulo depende de librerías diferentes.
PERFILES = {
    "agenda": "salidas.agenda",
    "banner": "salidas.banner",
    "inscripcion": "salidas.inscripcion",
}

perfil = os.getenv("PERFIL")
evento = os.getenv("EVENTO_NOMBRE", "Semana de la Ingenieria")

if perfil is None:
    print("No se sabe qué perfil ejecutar: falta configuración del contenedor.")
    raise SystemExit(1)

if perfil not in PERFILES:
    print(f"Perfil desconocido: {perfil}")
    raise SystemExit(1)

try:
    modulo = importlib.import_module(PERFILES[perfil])
except ModuleNotFoundError as error:
    print(f"El perfil '{perfil}' necesita la librería '{error.name}', "
          f"pero no está instalada en esta imagen.")
    raise SystemExit(1)

modulo.mostrar(evento)
