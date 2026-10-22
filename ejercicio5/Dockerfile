FROM python:3.12-alpine

ARG PERFIL

WORKDIR /app

COPY perfiles/ ./perfiles/
RUN case "$PERFIL" in \
    agenda|banner|inscripcion) ;; \
    *) echo >&2 "ERROR: PERFIL debe ser agenda, banner o inscripcion"; exit 1 ;; \
esac \
    && pip install --no-cache-dir -r "perfiles/${PERFIL}/requirements.txt" \
    && rm -rf perfiles

COPY app/ ./

ENV PERFIL=${PERFIL}

CMD ["python", "main.py"]
