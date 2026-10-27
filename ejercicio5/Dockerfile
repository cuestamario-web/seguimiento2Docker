FROM python:3.12-alpine

ARG PERFIL 
ENV PERFIL=${PERFIL}

WORKDIR /app

COPY perfiles/ /app/perfiles/

RUN if [ -z "$PERFIL" ] || [ ! -d "/app/perfiles/$PERFIL" ]; then \
	echo "Error: El perfil  '$PERFIL' no existe o no se especifico en --build-arg PERFIL." >&2; \
	exit 1; \
    fi

RUN pip install --no-cache-dir -r /app/perfiles/${PERFIL}/requirements.txt

COPY app/ /app/

CMD ["python", "main.py"]
