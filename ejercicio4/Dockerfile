
FROM alpine:3.20

ARG LENGUAJE=java

WORKDIR /app

RUN if [ "$LENGUAJE" = "java" ]; then \
        apk add --no-cache openjdk21-jdk; \
    elif [ "$LENGUAJE" = "python" ]; then \
        apk add --no-cache python3; \
    else \
        echo "ERROR: Lenguaje no soportado: $LENGUAJE. Use java o python."; \
        exit 1; \
    fi

COPY $LENGUAJE/ /app/

RUN if [ "$LENGUAJE" = "java" ]; then \
       javac src/conversor/*.java; \
    elif [ "$LENGUAJE" = "python" ]; then \
       python3 -m venv /app/.venv && \
       /app/.venv/bin/pip install --no-cache-dir -r requirements.txt;\
    fi

ENV MONEDA_DESTINO=USD
ENV LENGUAJE=$LENGUAJE
ENV PATH="/app/.venv/bin:$PATH"

CMD ["sh", "-c", "if [ \"$LENGUAJE\" = java ]; then exec java -cp out conversor.Main; else exec python3 app.py; fi"]

