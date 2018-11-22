FROM python

RUN pip install --no-cache-dir motor aiocontextvars faust
WORKDIR /app
COPY kafkamongodbstream.py /app
ENTRYPOINT python kafkamongodbstream.py worker
