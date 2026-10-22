FROM eclipse-temurin:21-jdk-alpine

# Crea y establece el directorio de trabajo
WORKDIR /app

# Copia todo el contenido
COPY . .

# Compila todos los archivos .java que estén dentro del paquete bodega
RUN javac src/bodega/*.java

# Ejecuta la aplicación compilada indicando el paquete (bodega.Main)
CMD ["java", "-cp", "src", "bodega.Main"]