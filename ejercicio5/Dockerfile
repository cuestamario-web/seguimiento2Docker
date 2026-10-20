FROM python:3.12-alpine

ARG PERFIL

WORKDIR /app

# Valida el perfil e instala SOLO sus librerías.
# El bind mount deja leer perfiles/ durante el build sin guardarlo en la imagen.
RUN --mount=type=bind,source=perfiles,target=/tmp/perfiles \
    if [ ! -f "/tmp/perfiles/${PERFIL}/requirements.txt" ]; then \
      echo "ERROR: el perfil '${PERFIL}' no existe. Perfiles disponibles: $(ls /tmp/perfiles | tr '\n' ' ')" >&2; \
      exit 1; \
    fi && \
    pip install --no-cache-dir -r /tmp/perfiles/${PERFIL}/requirements.txt

# El ARG solo existe durante el build; se guarda para que main.py lo lea al ejecutar
ENV PERFIL=${PERFIL}

COPY app/ ./

CMD ["python", "main.py"]