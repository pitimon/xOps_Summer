FROM python:3.7.3-alpine3.8
RUN apk add --no-cache build-base
WORKDIR /app
COPY ui.py .
COPY model.py .
COPY requirements.txt .
COPY templates templates
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--bind", ":80", "ui:app"]
