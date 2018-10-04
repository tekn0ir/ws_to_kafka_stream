FROM python:3.6

RUN pip install --no-cache-dir aiohttp aiocontextvars faust
WORKDIR /app
COPY poloniexstream.py /app
ENTRYPOINT python poloniexstream.py
