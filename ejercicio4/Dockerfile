FROM alpine:3.20

ARG LENGUAJE=java
ENV LENGUAJE=$LENGUAJE

WORKDIR /app

RUN if [ "$LENGUAJE" = "java" ]; then \
    apk add --no-cache openjdk21-jdk; \
    elif [ "$LENGUAJE" = "python" ]; then \
    apk add --no-cache python3; \
    else \
    echo "ERROR: lenguajes permitidos java y python, ingrese de nuevo el mensaje"; \
    fi

COPY $LENGUAJE/ /app/

RUN if [ "$LENGUAJE" = "java" ]; then \
    javac src/conversor/*.java; \
    else \
     python3 -m venv /app/.venv && \
        /app/.venv/bin/pip install --no-cache-dir -r requirements.txt;\
    fi

ENV MONEDA_DESTINO=EUR

ENV PATH="/usr/lib/jvm/default-jvm/bin:/app/.venv/bin:$PATH"

CMD sh -c "if [ \"$LENGUAJE\" = \"java\" ]; then exec java -cp src conversor.Main; else python app.py; fi"
