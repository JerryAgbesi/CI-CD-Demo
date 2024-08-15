#syntax=docker/dockerfile:1
FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY requirements.txt .

RUN apk update --no-cache \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir psycopg2-binary \
    && pip install --no-cache-dir -r requirements.txt \
    && apk add --no-cache libpq

COPY . . 

EXPOSE 9090

CMD python -m uvicorn src.app:app --host 0.0.0.0 --port 9090