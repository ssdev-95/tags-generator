# syntax=docker/dockerfile:1

FROM alpine:latest
WORKDIR /app

COPY .pylintrc .
COPY requirements.txt .
COPY run.py .
COPY src ./src

RUN mkdir ./tmp/
RUN apk update && apk add python3 py3-pip
RUN pip install -r requirements.txt --break-system-packages
RUN pylint *.py  --ignore-paths=./__tests__ --ignore=**/__init__.py -v
