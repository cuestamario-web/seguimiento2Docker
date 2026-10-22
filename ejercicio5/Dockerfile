FROM python:3.12-alpine

ARG PERFIL
ENV PERFIL=${PERFIL}

WORKDIR /app

COPY perfiles/ /tmp/perfiles/

RUN if [ -z "$PERFIL" ] || [ ! -d "/tmp/perfiles/$PERFIL" ]; then \
      echo "ERROR: el perfil '$PERFIL' no existe en perfiles/" >&2; \
      exit 1; \
    fi && \
    pip install --no-cache-dir -r /tmp/perfiles/$PERFIL/requirements.txt && \
    rm -rf /tmp/perfiles

COPY app/ ./

CMD ["python", "main.py"]