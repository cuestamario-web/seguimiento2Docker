FROM eclipse-temurin:21-jdk-alpine

WORKDIR /app

COPY src ./src
COPY datos ./datos

RUN javac -d bin src/bodega/*.java

CMD ["java", "-cp", "bin", "bodega.Main"]

