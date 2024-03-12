# Usa una imagen oficial de Node como imagen base
FROM node:20

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el package.json y el package-lock.json (si está disponible)
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto del código de la aplicación
COPY . .

# Exponer el puerto 8000 para el servidor de desarrollo (ajustar según necesidades)
EXPOSE 5173

# Comando para ejecutar la aplicación
CMD ["npm", "run", "dev"]
