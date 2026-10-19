FROM alpine:3.20

ARG LENGUAJE
ENV LENGUAJE_ENV=$LENGUAJE

RUN if [ "$LENGUAJE_ENV" != "java" ] && [ "$LENGUAJE_ENV" != "python" ]; then \
    echo "Error: El argumento LENGUAJE debe ser 'java' o 'python'." && exit 1; \
    fi

WORKDIR /app

RUN if [ "$LENGUAJE_ENV" = "java" ]; then \
    apk add --no-cache openjdk21-jdk; \
    elif [ "$LENGUAJE_ENV" = "python" ]; then \
    apk add --no-cache python3 py3-pip; \
    fi

COPY ${LENGUAJE_ENV}/ /app/

RUN if [ "$LENGUAJE_ENV" = "java" ]; then \
    mkdir -p bin && javac -d bin src/conversor/*.java; \
    elif [ "$LENGUAJE_ENV" = "python" ]; then \
    python3 -m venv venv && \   
    ./venv/bin/pip install --no-cache-dir -r requirements.txt; \
    fi

ENV MONEDA_DESTINO=USD

CMD ["sh", "-c", "if [ \"$LENGUAJE_ENV\" = \"java\" ]; then java -cp bin conversor.Main; else ./venv/bin/python app.py; fi"]