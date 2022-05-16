FROM python:3.7.3-alpine3.8
RUN apk add --no-cache mariadb-dev build-base
WORKDIR /app
COPY rpc.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD nameko run rpc --broker amqp://guest:guest@rabbitmq:5672
