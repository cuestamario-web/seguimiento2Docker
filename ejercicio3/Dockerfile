FROM eclipse-temurin:21-jdk-alpine

WORKDIR /app

COPY src ./src

COPY datos ./datos

RUN javac -d out src/bodega/*.java

ENV ARCHIVO_INVENTARIO=datos/inventario.txt

CMD ["java", "-cp", "out", "bodega.Main"]