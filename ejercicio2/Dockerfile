FROM node:20-alpine

WORKDIR /app

# Primero package.json para aprovechar la caché de capas al instalar dependencias
COPY package.json ./
RUN npm install --omit=dev

COPY src ./src

# La app escucha siempre en el 3000 (fijo en src/config.js)
EXPOSE 3000

# SEDE_CAFETERIA es OBLIGATORIA: no se define aquí a propósito,
# hay que pasarla con -e al hacer docker run.
CMD ["npm", "start"]
