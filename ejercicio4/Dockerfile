FROM alpine:3.20

ARG LENGUAJE

# Validar ANTES de copiar, para fallar con un mensaje claro
RUN case "$LENGUAJE" in \
      java|python) ;; \
      *) echo "ERROR: LENGUAJE debe ser 'java' o 'python' (se recibió: '$LENGUAJE')" >&2; exit 1 ;; \
    esac

# El ARG solo existe durante el build; se guarda para usarlo al ejecutar
ENV LENGUAJE=$LENGUAJE
ENV MONEDA_DESTINO=USD

WORKDIR /app

# Copia solo la carpeta del lenguaje elegido
COPY ${LENGUAJE}/ ./

RUN if [ "$LENGUAJE" = "java" ]; then \
      apk add --no-cache openjdk21-jdk && \
      mkdir out && \
      /usr/lib/jvm/default-jvm/bin/javac -d out $(find src -name "*.java"); \
    else \
      apk add --no-cache python3 && \
      python3 -m venv /opt/venv && \
      /opt/venv/bin/pip install --no-cache-dir -r requirements.txt; \
    fi

CMD ["sh", "-c", "if [ \"$LENGUAJE\" = \"java\" ]; then exec /usr/lib/jvm/default-jvm/bin/java -cp out conversor.Main; else exec /opt/venv/bin/python app.py; fi"]