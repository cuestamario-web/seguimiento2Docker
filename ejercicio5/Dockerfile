FROM python:3.12-alpine

ARG PERFIL
#NO tiene valor por defecto se agrega la que se ingresa como arg
ENV PERFIL=$PERFIL

WORKDIR /app

RUN if [ -z "$PERFIL" ]; then \
    echo "ERROR: Ingresa un perfil con --build-arg PEFIL =(agenda, banner, inscripcion)"; \
    fi

COPY perfiles/${PERFIL}/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

ENV EVENTO_NOMBRE="Semana de la ingenieria"

CMD ["python", "main.py"]

# C:\Users\morde\OneDrive\Desktop\seguimientoDocker\seguimiento2Docker\ejercicio5\perfiles\agenda\requirements.txt