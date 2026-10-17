# syntax=docker/dockerfile:1
FROM python:3.12-alpine

# agenda | banner | inscripcion
ARG PERFIL

WORKDIR /app

# Se monta perfiles/ solo durante este RUN (BuildKit): se valida el perfil e
# instalan SOLO sus librerías, sin dejar los requirements de otros perfiles en la imagen.
RUN --mount=type=bind,source=perfiles,target=/perfiles \
    if [ -z "$PERFIL" ] || [ ! -f "/perfiles/$PERFIL/requirements.txt" ]; then \
      echo "ERROR: el perfil '$PERFIL' no existe. Use --build-arg PERFIL=agenda | banner | inscripcion" >&2; \
      exit 1; \
    fi && \
    pip install --no-cache-dir -r "/perfiles/$PERFIL/requirements.txt"

COPY app/ .

# main.py lee PERFIL desde el entorno, por eso se pasa de ARG a ENV
ENV PERFIL=${PERFIL}

# Opcionales: EVENTO_NOMBRE (todos los perfiles) y URL_INSCRIPCION (solo inscripcion)
ENV EVENTO_NOMBRE="Semana de la Ingenieria"

CMD ["python", "main.py"]
