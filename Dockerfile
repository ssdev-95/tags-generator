FROM python:alpine
WORKDIR /app

COPY requirements.txt .
COPY run.py .
COPY src ./src
COPY tmp ./tmp

RUN pip install -r requirements.txt --break-system-packages
