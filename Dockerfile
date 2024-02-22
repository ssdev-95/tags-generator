FROM python:alpine
WORKDIR /app

COPY requirements.txt .
COPY run.py .
COPY src ./src
COPY tmp ./tmp
COPY __tests__ ./__tests__

RUN pip install -r requirements.txt --break-system-packages
