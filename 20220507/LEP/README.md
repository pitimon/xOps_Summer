https://blog.pjjop.org/how-to-set-lemp-stack-with-docker-containers/

# nginx+php /EP

docker network create web_network

docker-compose up -d
docker-compose ps

docker-compose down
docker-compose down --rmi all --volumes
