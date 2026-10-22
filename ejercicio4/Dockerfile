FROM alpine:3.20

ARG LENGUAJE

RUN if [ "$LENGUAJE" != "java" ] && [ "$LENGUAJE" != "python" ]; then \
    echo >&2 "ERROR: LENGUAJE debe ser java o python"; \
    exit 1; \
fi

RUN if [ "$LENGUAJE" = "java" ]; then \
    apk add --no-cache openjdk21-jdk; \
else \
    apk add --no-cache python3 py3-pip py3-virtualenv; \
fi

ENV PATH="/usr/lib/jvm/default-jvm/bin:${PATH}"
ENV MONEDA_DESTINO=USD

WORKDIR /app

COPY ${LENGUAJE} /app

RUN if [ "$LENGUAJE" = "java" ]; then \
    javac src/conversor/*.java; \
else \
    python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt; \
fi

ENV LENGUAJE=${LENGUAJE}

CMD ["sh", "-c", "if [ \"$LENGUAJE\" = \"java\" ]; then java -cp src conversor.Main; else /venv/bin/python app.py; fi"]