FROM python:3.7.4-alpine

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . app/
WORKDIR /app

