https://blog.pjjop.org/how-to-set-lemp-stack-with-docker-containers/

# nginx /Nginx

docker network create web_network
docker network ls

docker-compose up -d

docker-compose down --rmi all

# nginx+php /EP

docker-compose up -d
docker-compose ps
docker-compose down --rmi all

# nginx+MariaDB+php /LEMP
docker network create web_network
docker-compose build

docker-compose up -d  
docker-compose down

