FROM debian:stable

WORKDIR /var/www

RUN apt-get update
RUN apt-get -y --no-install-recommends install curl
RUN apt-get -y --no-install-recommends install ca-certificates

RUN curl https://raw.githubusercontent.com/gadiener/docker-images-size-benchmark/master/main.go -o main.go

RUN apt-get purge -y curl
RUN apt-get purge -y ca-certificates
RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
