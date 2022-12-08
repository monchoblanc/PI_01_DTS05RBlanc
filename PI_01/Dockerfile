#de hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/
#VER QUE LE TENGO Q AGREGAR O MODIFICAR!!!
FROM python:3.9

COPY . usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt   

ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload