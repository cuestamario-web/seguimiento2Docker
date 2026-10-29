FROM python:3.12-alpine

ARG PERFIL

WORKDIR /app

RUN --mount=type=bind,source=perfiles,target=/perfiles \
    if [ -z "$PERFIL" ] || [ ! -d "/perfiles/$PERFIL" ]; then \
      echo "ERROR: el perfil '$PERFIL' no existe. Use --build-arg PERFIL=<agenda|banner|inscripcion>" >&2; \
      exit 1; \
    fi && \
    pip install --no-cache-dir -r /perfiles/$PERFIL/requirements.txt

ENV PERFIL=${PERFIL}

COPY app/ ./

CMD ["python", "main.py"]