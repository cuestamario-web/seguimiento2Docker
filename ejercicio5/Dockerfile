FROM python:3.12-alpine

ARG PERFIL

# Copia la carpeta de perfiles para poder validarla
COPY perfiles/ /perfiles/

# 1 Valida si el perfil existe falla  si no
# 2 Si existe, instala solo ese requirements.txt
# 3 Borra la carpeta temporal de perfiles para no hacer bulto
RUN if [ ! -d "/perfiles/$PERFIL" ]; then \
      echo "ERROR: El perfil '$PERFIL' no existe. Usa agenda, banner o inscripcion." && exit 1; \
    fi && \
    pip install --no-cache-dir -r /perfiles/$PERFIL/requirements.txt && \
    rm -rf /perfiles

# Define la variable de entorno para que main.py sepa que perfil ejecutar
ENV PERFIL=${PERFIL}

# Define el directorio de trabajo y copia el codigo de la app
WORKDIR /app
COPY app/ .

# Ejecuta el programa
CMD ["python", "main.py"]