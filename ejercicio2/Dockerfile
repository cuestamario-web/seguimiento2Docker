# Usa una imagen oficial ligera de Node.js
FROM node:18-alpine

# Crea y establece el directorio de trabajo
WORKDIR /app

COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto del código de la aplicación
COPY . .

CMD ["node", "src/server.js"]