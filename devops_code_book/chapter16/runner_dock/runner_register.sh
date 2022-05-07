#!/bin/sh
# Get the registration token

registration_token=xxxxxxxxxxxxxxx

docker exec -it gitlab-runner1 \
  gitlab-runner register \
    --non-interactive \
    --docker-privileged \
    --registration-token ${registration_token} \
    --locked=false \
    --description docker-stable \
    --url https://gitlab.lab20.cpsudevops.com/ \
    --executor docker \
    --docker-image docker:stable \
    --docker-volumes "/var/run/docker.sock:/var/run/docker.sock" \
    --docker-network-mode gitlab_network
    