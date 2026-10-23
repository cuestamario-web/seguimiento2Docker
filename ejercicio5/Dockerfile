FROM python:3.12-alpine

ARG PERFIL

WORKDIR /app

COPY perfiles ./perfiles

RUN if [ -z "$PERFIL" ] || [ ! -f "perfiles/$PERFIL/requirements.txt" ]; then \
        echo "ERROR: el perfil '$PERFIL' no existe. Perfiles validos: $(ls perfiles | tr '\n' ' ')"; \
        exit 1; \
    fi && \
    pip install --no-cache-dir -r "perfiles/$PERFIL/requirements.txt" && \
    rm -rf perfiles

ENV PERFIL=${PERFIL}

ENV EVENTO_NOMBRE="Semana de la Ingenieria"

COPY app/ ./

CMD ["python", "main.py"]