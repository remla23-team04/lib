# Dockerfile
FROM python:3.7-slim
WORKDIR /root
COPY requirements.txt /root/
RUN pip install -r requirements.txt
