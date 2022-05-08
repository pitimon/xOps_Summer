https://blog.pjjop.org/how-to-set-lemp-stack-with-docker-containers/
option: mysqladmin service add

# nginx+MariaDB+php /LEMP

docker network create web_network
# build Dockerfile (php)
docker-compose build
# container daemin start 
docker-compose up -d

# container list process
docker-compose ls
docker-compose ps
- portainer is clear more.


# down container only
docker-compose down
# down and remove images volumes
docker-compose down --rmi all  --volumes

