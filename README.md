
Clonar el repositorio,
Se debetener en cuenta, que el proyecto cuenta con una imagen de docker, por lo que es necesario tener habilitado un lector de imagen docker en la maquina.

#Para inicializar el Docker:

docker-compose -f local.yml  build
docker-compose -f local.yml  up

#Creamos un superusuario

docker-compose -f local.tml run --rm django python manage.py cratesuperuser

El proyecto cuenta con dos urls bases, como la creacion de productos y de comercios (se refiere a una sucursal de la tienda)

