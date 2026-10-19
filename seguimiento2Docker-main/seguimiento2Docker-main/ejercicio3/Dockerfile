FROM eclipse-temurin:21-jdk-alpine

WORKDIR /app

COPY . .

RUN mkdir -p bin && javac -d bin src/bodega/*.java

CMD ["java", "-cp", "bin", "bodega.Main"]