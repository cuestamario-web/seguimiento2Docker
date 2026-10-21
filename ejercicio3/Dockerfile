FROM eclipse-temurin:21-jdk-alpine

WORKDIR /app

COPY src ./
COPY datos ./datos

RUN javac bodega/*.java

CMD ["java", "bodega.Main"]