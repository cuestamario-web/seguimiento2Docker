FROM python:3.12-alpine

ARG PERFIL

WORKDIR /app

COPY perfiles/ /tmp/perfiles/
RUN if [ ! -f "/tmp/perfiles/${PERFIL}/requirements.txt" ]; then \
        echo "ERROR: el perfil '${PERFIL}' no existe. Use: agenda, banner o inscripcion"; \
        exit 1; \
    fi && \
    pip install --no-cache-dir -r /tmp/perfiles/${PERFIL}/requirements.txt && \
    rm -rf /tmp/perfiles

COPY app/ ./

ENV PERFIL=${PERFIL}

CMD ["python", "main.py"]