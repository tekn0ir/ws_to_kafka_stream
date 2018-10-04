FROM python

RUN pip install --no-cache-dir aiohttp aiocontextvars faust
WORKDIR /app
COPY websocketstream.py /app
ENTRYPOINT python websocketstream.py
