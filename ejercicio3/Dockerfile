FROM eclipse-temurin:21-jdk-alpine

WORKDIR /app

COPY src ./src

COPY datos ./datos

RUN mkdir out && javac -d out src/bodega/*.java

CMD ["java", "-cp", "out", "bodega.Main"]
