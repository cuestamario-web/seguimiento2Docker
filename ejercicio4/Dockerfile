FROM alpine:3.20

ARG LENGUAJE

RUN if [ "$LENGUAJE" != "java" ] && [ "$LENGUAJE" != "python" ]; then \
      echo "ERROR: LENGUAJE debe ser 'java' o 'python' (recibido: '$LENGUAJE')" >&2; \
      exit 1; \
    fi

ENV LENGUAJE=${LENGUAJE}

ENV MONEDA_DESTINO=USD

WORKDIR /app

COPY ${LENGUAJE}/ ./

RUN if [ "$LENGUAJE" = "java" ]; then \
      apk add --no-cache openjdk21-jdk && \
      mkdir out && \
      /usr/lib/jvm/default-jvm/bin/javac -d out src/conversor/*.java ; \
    else \
      apk add --no-cache python3 && \
      python3 -m venv /opt/venv && \
      /opt/venv/bin/pip install --no-cache-dir -r requirements.txt ; \
    fi

CMD if [ "$LENGUAJE" = "java" ]; then \
      exec /usr/lib/jvm/default-jvm/bin/java -cp out conversor.Main ; \
    else \
      exec /opt/venv/bin/python app.py ; \
    fi