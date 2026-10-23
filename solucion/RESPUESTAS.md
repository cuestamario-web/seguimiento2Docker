# Seguimiento 2 Docker — Respuestas y comandos

> Todos los comandos se ejecutan desde la carpeta `seguimiento2Docker/`.
> Cada `docker build` usa como contexto la carpeta del ejercicio.

---

## Ejercicio 1 — Reporte de notas (Python)

**Dockerfile:** `FROM python:3.12-alpine` → copia `app.py`, `evaluacion.py`, `notas.csv` → `ENV NOTA_APROBACION=3.0` → `CMD ["python","app.py"]`.

**Preguntas**
- ¿Usa variable de entorno? Sí: `NOTA_APROBACION` (en `evaluacion.py`: `float(os.getenv("NOTA_APROBACION", "3.0"))`).
- ¿Es obligatoria? No. Si no se define se usa el valor por defecto `3.0`.
- ¿Qué cambia? La nota mínima para aprobar. Con 3.0 aprueban 5 de 7; con 3.5 aprueban 2 de 7 (las definitivas no cambian, solo el estado APROBADO/REPROBADO).

**Comandos**
```bash
docker build -t ej1-notas ./ejercicio1
docker run --rm ej1-notas                                  # umbral 3.0 -> 5 de 7 aprobados
docker run --rm -e NOTA_APROBACION=3.5 ej1-notas           # umbral 3.5 -> 2 de 7 aprobados
```

---

## Ejercicio 2 — API de la cafetería (Node.js)

**Dockerfile:** `FROM node:20-alpine` → copia `package.json` y hace `npm install --omit=dev` (capa cacheable) → copia `src/` → `EXPOSE 3000` → `CMD ["node","src/server.js"]`.

**Preguntas**
- Puerto: **3000** (fijo en `src/config.js`, no es configurable).
- Variable de entorno: `SEDE_CAFETERIA`.
- ¿Obligatoria? **Sí.** Si no se define, `config.js` imprime "configuración incompleta" y hace `process.exit(1)`: el contenedor arranca y se detiene de inmediato.

**Comandos**
```bash
docker build -t ej2-cafeteria ./ejercicio2

# Un contenedor (puerto 3000 del contenedor -> 3000 de tu PC)
docker run -d --name cafe-centro -p 3000:3000 -e SEDE_CAFETERIA="Centro" ej2-cafeteria
# Navegador: http://localhost:3000/   http://localhost:3000/menu   http://localhost:3000/menu/bebidas

# Dos sedes a la vez: mismo puerto interno (3000), distinto puerto en tu equipo
docker rm -f cafe-centro
docker run -d --name cafe-norte -p 3001:3000 -e SEDE_CAFETERIA="Norte" ej2-cafeteria
docker run -d --name cafe-sur   -p 3002:3000 -e SEDE_CAFETERIA="Sur"   ej2-cafeteria
# http://localhost:3001/  -> "Bienvenido a la cafetería Norte"
# http://localhost:3002/  -> "Bienvenido a la cafetería Sur"

# Prueba de que es obligatoria (se detiene con error)
docker run --rm ej2-cafeteria

# Limpieza
docker rm -f cafe-norte cafe-sur
```

---

## Ejercicio 3 — Inventario de bodega (Java)

**Dockerfile:** `FROM eclipse-temurin:21-jdk-alpine` → copia `src/` y `datos/` → `javac -d out src/bodega/*.java` → `ENV ARCHIVO_INVENTARIO=datos/inventario.txt` → `CMD ["java","-cp","out","bodega.Main"]`.

**Preguntas**
- Archivos además del código: la carpeta `datos/` (los `.txt` de inventario), porque `LectorInventario` los lee en tiempo de ejecución.
- Variable de entorno: `ARCHIVO_INVENTARIO`.
- ¿Obligatoria? No (por defecto `datos/inventario.txt`). Sirve para elegir qué archivo de inventario se lee. Si el archivo no existe, la app imprime error y sale con código 1.

**Comandos**
```bash
docker build -t ej3-bodega ./ejercicio3
docker run --rm ej3-bodega                                                         # inventario general
docker run --rm -e ARCHIVO_INVENTARIO=datos/inventario_sede_norte.txt ej3-bodega   # sede norte
```

---

## Ejercicio 4 — Conversor de monedas (un Dockerfile, dos lenguajes)

**Dockerfile:** `FROM alpine:3.20` con `ARG LENGUAJE`:
1. Valida primero: si no es `java` ni `python`, `exit 1` con mensaje claro.
2. Instala `openjdk21-jdk` (java) o `python3` (python).
3. `COPY ${LENGUAJE}/ ./` copia solo la carpeta elegida.
4. Java: compila con `javac` → `out/`. Python: `python3 -m venv /opt/venv` + `pip install -r requirements.txt` (tabulate).
5. `ENV LENGUAJE` y `ENV MONEDA_DESTINO=USD`; el `CMD` ejecuta el programa correcto según `LENGUAJE`.

**Pregunta:** ambos proyectos usan `MONEDA_DESTINO`; acepta `USD`, `EUR` o `MXN` (por defecto USD). Cualquier otro valor imprime "Moneda no soportada" y termina con código 1.

**Comandos**
```bash
docker build --build-arg LENGUAJE=java   -t conversor-java   ./ejercicio4
docker build --build-arg LENGUAJE=python -t conversor-python ./ejercicio4

docker run --rm conversor-java                                   # USD (por defecto)
docker run --rm -e MONEDA_DESTINO=EUR conversor-java
docker run --rm -e MONEDA_DESTINO=MXN conversor-java

docker run --rm conversor-python
docker run --rm -e MONEDA_DESTINO=EUR conversor-python
docker run --rm -e MONEDA_DESTINO=MXN conversor-python

# Prueba del error de construcción (debe fallar con mensaje claro)
docker build --build-arg LENGUAJE=ruby -t conversor-ruby ./ejercicio4
```

---

## Ejercicio 5 — Un proyecto, varios perfiles de librerías (Python)

**Dockerfile:** `FROM python:3.12-alpine` con `ARG PERFIL`:
1. Copia `perfiles/` a `/tmp/perfiles` (solo archivos de texto) y verifica que exista `perfiles/$PERFIL/requirements.txt`; si no, falla con mensaje claro.
2. Instala **solo** el requirements de ese perfil y borra `/tmp/perfiles`.
3. `ENV PERFIL=${PERFIL}` y `ENV EVENTO_NOMBRE="Semana de la Ingenieria"`.
4. Copia `app/` y ejecuta `python main.py`.

**Preguntas**
- ¿Cómo sabe `main.py` el perfil? Lee la variable de entorno `PERFIL` (`os.getenv("PERFIL")`). Un `ARG` solo existe durante el build, por eso hay que pasarlo a `ENV PERFIL=${PERFIL}` para que exista al ejecutar el contenedor. Si falta, imprime "No se sabe qué perfil ejecutar" y sale con 1.
- Otras variables (todas opcionales):
  - `EVENTO_NOMBRE` (por defecto "Semana de la Ingenieria"): la usan los tres perfiles.
  - `URL_INSCRIPCION` (por defecto `https://eam.edu.co`): solo el perfil `inscripcion`.
- Ejecutar la imagen `agenda` con `-e PERFIL=banner`: `main.py` intenta importar `salidas.banner`, que necesita `pyfiglet` y `colorama`, pero esa imagen solo tiene `tabulate`. Se produce `ModuleNotFoundError`, que el código captura e imprime "El perfil 'banner' necesita la librería 'pyfiglet', pero no está instalada en esta imagen." y sale con código 1. La variable de entorno cambia qué módulo se intenta ejecutar, pero no puede instalar librerías: eso se decide en el build.

**Comandos**
```bash
docker build --build-arg PERFIL=agenda      -t evento-agenda      ./ejercicio5
docker build --build-arg PERFIL=banner      -t evento-banner      ./ejercicio5
docker build --build-arg PERFIL=inscripcion -t evento-inscripcion ./ejercicio5

docker run --rm evento-agenda
docker run --rm evento-banner
docker run --rm evento-inscripcion
docker run --rm -e URL_INSCRIPCION=https://ejemplo.com -e EVENTO_NOMBRE="Feria de Software" evento-inscripcion

# Comparar tamaños
docker images --filter "reference=evento-*"

# Pregunta 4: imagen agenda ejecutada como banner
docker run --rm -e PERFIL=banner evento-agenda

# Prueba del error de construcción
docker build --build-arg PERFIL=otro -t evento-otro ./ejercicio5
```

---

## Entrega (según README)
```bash
git checkout -b tu-nombre-apellido
git add .
git commit -m "Solución seguimiento 2 Docker"
git push -u origin tu-nombre-apellido
```
