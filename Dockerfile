# syntax=docker/dockerfile:1

FROM python:slim-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "hello_world.py"]