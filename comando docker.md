`docker pull NOMBRE_IMG` > descarga desde el docker hub la imagen indicada, adicional a ello le puedo colocar la version (etiqueta) en especifico

`docker images` > muestra todas las imagenes que he descargado y que estan listas para ser utilizadas en mis contenedores

`docker image rm NOMBRE_IMG:TAG` > elimina y libera el espacio ocupado por la imagen de docker

`docker create NOMBRE_IMG:TAG` > busca si tenemos la imagen, sino, la descarga de docker hub y crea el contenedor con esa imagen seleccionada

`docker ps` > muestra los contenedores activos

`docker ps --all` > muestra los contenedores activos y los inactivos

`docker start ID` > inicializa el contenedor con sus imagenes correspondientes

`docker logs NOMBRE_CONTENEDOR` > muestra los logs (eventos) que han sucedido dentro del contenedor

`docker logs --follow NOMBRE_CONTENEDOR` > muestra los logs y ademas se mantiene escuchando los nuevos logs

`docker stop ID` > detiene el contenedor y lo pasa a un estado inactivo

`docker rm NOMBRE_CONTENEDOR` > elimina el contenedor (inactivo) y se pierden sus datos y toda su informacion a no ser que estemos usando volumes

`docker create --name NOMBRE_PERSONALIZADO NOMBRE_IMG:TAG` > crea un contenedor con un nombre especifico para una mejor descripcion del contenedor

`docker create ... -pPUERTO_LOCAL:PUERTO_CONTENDOR ... ` > crea un contenedor una puerta de acceso para poder ingresar a la informacion dentro del contenedor

Si me quiero evitar todos los pasos anteriores y solamente ejecutar un solo comando entonces uso el `docker run`

`docker run --name NOMBRE_CONTENEDOR -pPUERTO_LOCAL:PUERTO_CONTENEDOR -d NOMBRE_IMG` > -d es deatached y sirve para indicar que el cotenedor se ejecutara en segundo plano (background)

`docker compose up` > Lee el archivo docker-compose y ejecuta los comandos internos
