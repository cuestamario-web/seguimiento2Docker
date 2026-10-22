FROM alpine:3.20

ARG LENGUAJE

# 1 Validar el lenguaje 
RUN if [ "$LENGUAJE" != "java" ] && [ "$LENGUAJE" != "python" ]; then \
      echo "ERROR: El LENGUAJE debe ser estrictamente java o python" && exit 1; \
    fi

WORKDIR /app

# 2 Instalar herramientas según el lenguaje
RUN if [ "$LENGUAJE" = "java" ]; then \
    apk add --no-cache openjdk21-jdk; \
    else \
      apk add --no-cache python3; \
    fi

# 3 Copiar únicamente la carpeta del lenguaje elegido usando la variable
COPY ${LENGUAJE} ./${LENGUAJE}

# 4. Preparar el proyecto usando las rutas completas del JDK o venv (según las pistas)
RUN if [ "$LENGUAJE" = "java" ]; then \
      /usr/lib/jvm/default-jvm/bin/javac ${LENGUAJE}/src/conversor/*.java; \
    else \
      python3 -m venv venv && \
      venv/bin/pip install -r ${LENGUAJE}/requirements.txt; \
    fi

# 5 Definir la variable de entorno por defecto (Punto 3)
ENV MONEDA_DESTINO="USD"

# 6 Guardar el lenguaje en el entorno para usarlo en el CMD al arrancar
ENV EXEC_LANG=$LENGUAJE

# 7 Ejecutar el programa correspondiente
CMD if [ "$EXEC_LANG" = "java" ]; then \
      /usr/lib/jvm/default-jvm/bin/java -cp java/src conversor.Main; \
    else \
      venv/bin/python python/app.py; \
    fi