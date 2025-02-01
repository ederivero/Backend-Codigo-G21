# INDICAR LA CONFIGURACION DE MI PROYECTO COMO IMAGEN DE DOCKER
FROM node:22.13

# Crea el directorio donde se alojara mi aplicacion
RUN mkdir -p /home/app

# Agarra y configura como la ruta de trabajo esta direccion dentro del contenedor
WORKDIR /home/app

# Copia todo el contenido del directorio actual al directorio del contenedor
COPY /src ./src
COPY package*.json ./

ENV PORT 3000
# Expongo el puerto desde mi contenedor interno hacia mi maquina
EXPOSE 3000


RUN npm i

# Este sera el comando que ejecutara el proyecto dentro del contenedor
CMD ["npm", "run", "start"]