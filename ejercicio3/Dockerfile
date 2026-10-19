FROM eclipse-temurin:21-jdk-alpine
WORKDIR /app
COPY src/ ./src/
COPY datos/ ./datos/
RUN find src -name "*.java" | xargs javac
ENV ARCHIVO_INVENTARIO="datos/inventario.txt"
CMD ["java", "-cp", "src", "bodega.Main"]