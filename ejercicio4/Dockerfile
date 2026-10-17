FROM alpine:3.20

# java | python
ARG LENGUAJE

# 1) Validar el argumento: si no es java ni python, la construcción falla
RUN case "$LENGUAJE" in \
      java|python) ;; \
      *) echo "ERROR: LENGUAJE='$LENGUAJE' no es válido. Use --build-arg LENGUAJE=java o LENGUAJE=python" >&2; exit 1 ;; \
    esac

# 2) Instalar solo lo necesario para ese lenguaje
RUN if [ "$LENGUAJE" = "java" ]; then \
      apk add --no-cache openjdk21-jdk; \
    else \
      apk add --no-cache python3; \
    fi

WORKDIR /app

# 3) Copiar únicamente la carpeta del proyecto elegido
COPY ${LENGUAJE}/ /app/

# 4) Preparar el proyecto: compilar (Java) o crear venv e instalar dependencias (Python)
RUN if [ "$LENGUAJE" = "java" ]; then \
      mkdir out && /usr/lib/jvm/default-jvm/bin/javac -d out src/conversor/*.java; \
    else \
      python3 -m venv venv && venv/bin/pip install --no-cache-dir -r requirements.txt; \
    fi

# Moneda destino (USD, EUR o MXN); ambos proyectos leen MONEDA_DESTINO
ENV MONEDA_DESTINO=USD

# ARG no existe en tiempo de ejecución, por eso se guarda también como ENV
ENV LENGUAJE=${LENGUAJE}

# 5) Ejecutar el programa correcto
CMD ["sh", "-c", "if [ \"$LENGUAJE\" = \"java\" ]; then exec /usr/lib/jvm/default-jvm/bin/java -cp out conversor.Main; else exec /app/venv/bin/python app.py; fi"]
