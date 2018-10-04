FROM python:3.6

RUN pip install --no-cache-dir websockets
WORKDIR /app
COPY testproducer.py /app
ENTRYPOINT python testproducer.py
