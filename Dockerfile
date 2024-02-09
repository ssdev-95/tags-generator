# syntax=docker/dockerfile:1

FROM python:3.11-alpine
WORKDIR /app

COPY requirements.txt .
COPY run.py .
COPY src ./src
COPY __tests__ ./__tests__

RUN mkdir ./tmp/
RUN pip install -r requirements.txt
CMD python3 run.py
