FROM python:3.12-alpine


ARG PERFIL


ENV PERFIL=${PERFIL}


ENV EVENTO_NOMBRE="Semana de la Ingenieria"
ENV URL_INSCRIPCION="https://eam.edu.co"

WORKDIR /app


COPY perfiles/ /tmp/perfiles/


RUN if [ ! -f "/tmp/perfiles/$PERFIL/requirements.txt" ]; then \
      echo "ERROR: el perfil '$PERFIL' no existe. Use --build-arg PERFIL=agenda|banner|inscripcion" >&2; \
      exit 1; \
    fi && \
    pip install --no-cache-dir -r "/tmp/perfiles/$PERFIL/requirements.txt" && \
    rm -rf /tmp/perfiles


COPY app/ ./

CMD ["python", "main.py"]