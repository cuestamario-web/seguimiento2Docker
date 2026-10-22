FROM python:3.12-alpine

ARG PERFIL=agenda

WORKDIR /app

RUN --mount=type=bind,source=perfiles,target=/tmp/perfiles \
    if [ "$PERFIL" = "agenda" ] || \
       [ "$PERFIL" = "banner" ] || \
       [ "$PERFIL" = "inscripcion" ]; then \
        pip install --no-cache-dir -r /tmp/perfiles/$PERFIL/requirements.txt; \
    else \
        echo "ERROR: Perfil no soportado. Use agenda, banner o inscripcion."; \
        exit 1; \
    fi

COPY app/ /app/

ENV PERFIL=${PERFIL}
ENV EVENTO_NOMBRE="Semana de la Ingenieria"
ENV URL_INSCRIPCION="https://eam.edu.co"


CMD ["python", "main.py"]
