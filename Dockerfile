FROM python:3.7.3-slim

COPY requirements.txt /

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt


COPY . /app

WORKDIR /app/passwordgenerator

EXPOSE 8084



CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]