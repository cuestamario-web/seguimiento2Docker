FROM eclipse-temurin:17-alpine

WORKDIR /app

COPY src ./

RUN javac bodega/*.java

COPY . .

CMD ["java","bodega.Main"]