FROM python:3.12-alpine

ARG PERFIL=agenda
ENV PERFIL=$PERFIL

WORKDIR /app

COPY perfiles/ /app/perfiles/

RUN if [ ! -d "/app/perfiles/$PERFIL" ]; then \
    echo "Error: El perfil '$PERFIL' no existe en la carpeta perfiles/." && exit 1; \
    fi

RUN pip install --no-cache-dir -r /app/perfiles/$PERFIL/requirements.txt

COPY app/ /app/
CMD ["python", "main.py"]