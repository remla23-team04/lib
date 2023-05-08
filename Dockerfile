FROM python:3.8-slim
WORKDIR /root
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
