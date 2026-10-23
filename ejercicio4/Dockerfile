FROM alpine:3.20

ARG LENGUAJE

RUN if [ "$LENGUAJE" != "java" ] && [ "$LENGUAJE" != "python" ]; then \
        echo "ERROR: LENGUAJE debe ser 'java' o 'python' (se recibio: '$LENGUAJE')"; \
        exit 1; \
    fi

RUN if [ "$LENGUAJE" = "java" ]; then \
        apk add --no-cache openjdk21-jdk; \
    else \
        apk add --no-cache python3; \
    fi

ENV PATH="/usr/lib/jvm/default-jvm/bin:/app/venv/bin:${PATH}"

WORKDIR /app

COPY ${LENGUAJE}/ ./

RUN if [ "$LENGUAJE" = "java" ]; then \
        javac -d out src/conversor/*.java && \
        echo "exec java -cp /app/out conversor.Main" > /app/iniciar.sh; \
    else \
        python3 -m venv venv && \
        venv/bin/pip install --no-cache-dir -r requirements.txt && \
        echo "exec python /app/app.py" > /app/iniciar.sh; \
    fi

ENV MONEDA_DESTINO=USD

    CMD ["sh", "/app/iniciar.sh"]