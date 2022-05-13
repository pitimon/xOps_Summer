FROM python:3.7

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]

HEALTHCHECK --interval=15s --timeout=3s \

CMD curl -f http://localhost:5000/ || exit 1