docker image build -t imageformfile:0.1 .

docker container run imageformfile:0.1

docker images
docker images history <image ID>

# edit Dockerfile in CMD ["figlet", "hello ......"] line.
docker image build -t imageformfile:0.2 .

docker container run imageformfile:0.2

docker images
docker images history <image ID>