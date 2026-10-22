FROM alpine:3.20

ARG LENGUAJE

WORKDIR /app


RUN if [ "$LENGUAJE" = "java" ]; then \
        apk add --no-cache openjdk21-jdk; \
    elif [ "$LENGUAJE" = "python" ]; then \
        apk add --no-cache python3; \
    else \
        echo "ERROR: LENGUAJE debe ser 'java' o 'python' (valor recibido: '$LENGUAJE')"; \
        exit 1; \
    fi


COPY . /tmp/contexto/
RUN cp -r /tmp/contexto/${LENGUAJE}/. /app/ && rm -rf /tmp/contexto


RUN if [ "$LENGUAJE" = "java" ]; then \
        mkdir out && /usr/lib/jvm/default-jvm/bin/javac -d out src/conversor/*.java; \
    else \
        python3 -m venv /opt/venv && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt; \
    fi


ENV LENGUAJE=${LENGUAJE}
ENV MONEDA_DESTINO=USD


CMD if [ "$LENGUAJE" = "java" ]; then \
        exec /usr/lib/jvm/default-jvm/bin/java -cp out conversor.Main; \
    else \
        exec /opt/venv/bin/python app.py; \
    fi