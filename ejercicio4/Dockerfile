FROM alpine:3.20

ARG LENGUAJE
ENV LENGUAJE=${LENGUAJE}
ENV MONEDA_DESTINO=USD
ENV PATH="/usr/lib/jvm/default-jvm/bin:${PATH}"

WORKDIR /app

RUN if [ "$LENGUAJE" != "java" ] && [ "$LENGUAJE" != "python" ]; then \
      echo " LENGUAJE debe ser 'java' o 'python' (recibido: '$LENGUAJE')" >&2; \
      exit 1; \
    fi

COPY ${LENGUAJE}/ ./

RUN if [ "$LENGUAJE" = "java" ]; then \
      apk add --no-cache openjdk21-jdk && \
      mkdir out && javac -d out src/conversor/*.java; \
    else \
      apk add --no-cache python3 && \
      python3 -m venv /opt/venv && \
      /opt/venv/bin/pip install --no-cache-dir -r requirements.txt; \
    fi

CMD ["sh", "-c", "if [ \"$LENGUAJE\" = \"java\" ]; then exec java -cp out conversor.Main; else exec /opt/venv/bin/python app.py; fi"]