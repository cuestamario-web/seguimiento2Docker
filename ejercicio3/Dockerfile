FROM eclipse-temurin:21-jdk-alpine

WORKDIR /app

COPY src ./src
COPY datos ./datos

RUN mkdir out && javac -d out src/bodega/*.java

# Archivo de inventario a leer (opcional, por defecto el de la sede principal)
ENV ARCHIVO_INVENTARIO=datos/inventario.txt

CMD ["java", "-cp", "out", "bodega.Main"]
