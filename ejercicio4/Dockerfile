# ---------- Etapa 1: validar LENGUAJE y separar el proyecto elegido ----------
FROM alpine:3.20 AS fuente
ARG LENGUAJE
COPY . /ctx
RUN case "$LENGUAJE" in \
      java|python) ;; \
      *) echo "ERROR: el argumento LENGUAJE debe ser 'java' o 'python' (valor recibido: '$LENGUAJE')" >&2; exit 1 ;; \
    esac && \
    mkdir /proyecto && cp -r "/ctx/$LENGUAJE/." /proyecto/


FROM alpine:3.20


ARG LENGUAJE


ENV MONEDA_DESTINO=USD

ENV LENGUAJE=${LENGUAJE}


RUN case "$LENGUAJE" in \
      java)   apk add --no-cache openjdk21-jdk ;; \
      python) apk add --no-cache python3 ;; \
      *)      echo "ERROR: el argumento LENGUAJE debe ser 'java' o 'python' (valor recibido: '$LENGUAJE')" >&2; exit 1 ;; \
    esac

WORKDIR /app


COPY --from=fuente /proyecto/ ./


RUN if [ "$LENGUAJE" = "java" ]; then \
      mkdir out && /usr/lib/jvm/default-jvm/bin/javac -d out $(find src -name "*.java"); \
    else \
      python3 -m venv venv && ./venv/bin/pip install --no-cache-dir -r requirements.txt; \
    fi


   CMD ["sh", "-c", "if [ \"$LENGUAJE\" = \"java\" ]; then /usr/lib/jvm/default-jvm/bin/java -cp out conversor.Main; else ./venv/bin/python app.py; fi"]