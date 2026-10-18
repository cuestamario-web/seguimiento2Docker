FROM node:20-alpine

WORKDIR /app

COPY package.json ./

ENV SEDE_CAFETERIA=ARMENIA

RUN npm install

COPY src ./src

EXPOSE 3000

CMD ["npm", "start"]


