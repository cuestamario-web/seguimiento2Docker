FROM alpine:3.20

ARG LENGUAJE

ENV LENGUAJE=${LENGUAJE} 
ENV MONEDA_DESTINO="USD"

WORKDIR /app 

RUN  if [ "$LENGUAJE" = "java" ]; then \
	apk add --no-cache openjdk21-jdk; \
     elif [ "$LENGUAJE" = "python" ]; then \
	apk add --no-cache python3 py3-pip; \
     else  \
	echo "Error: LENGUAJE invalido ('$LENGUAJE'). Debe ser 'java' o 'python'.">&2; \
	exit 1; \
     fi

COPY ${LENGUAJE} /app

RUN if [ "$LENGUAJE" = "java" ]; then \
	mkdir -p bin && javac -d bin src/conversor/*.java; \
    elif [ "$LENGUAJE" = "python" ]; then \
	python3 -m venv /opt/venv && \
	/opt/venv/bin/pip install --no-cache-dir -r requirements.txt; \
    fi

ENV PATH="/opt/venv/bin:/usr/lib/jvm/default-jvm/bin:$PATH"

CMD if [ "$LENGUAJE" = "java" ]; then \
	java -cp bin conversor.Main; \
    elif [ "$LENGUAJE" = "python" ]; then \
	python3 app.py; \
   fi


