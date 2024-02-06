# Building sirve para que despues de descargar el proyecto se ejecute el contenedor cuando es desde un equipo diferente o se borro el anteriormente creado

docker-compose up 

# Entrar en el root del contenedor sirve para poder ejecutrar comandos de administrador del contenedor del proyecto y desde aqui se pueden hacer las migraciones

docker exec -it django_container bash

# Ejecutar migraciones de models y demas cambiosde la parte del backend o de instalacion de plugins o frameworks

python manage.py make migrations

python manage.py migrate

# Comando para aceptar EULA de la base de datos de microsft para su ejecucion desde docker el nombre al final de "ramonuriel123" es el usuario de docker hub y el "/" es el nombre del repositorio y el nombre de "bderp" es e nombre del proyecto de la base de datos

docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Ramon200132" -p 1433:1433 -d ramonuriel123/bd:bderp