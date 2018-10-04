#!/usr/bin/env python
import traceback
import logging
import asyncio
import aiohttp
import faust
import os
import time

TOPIC = os.getenv('TOPIC', 'test')
BROKER = os.getenv('BROKER', 'kafka://kafka:9092')
URL = os.getenv('URL', 'ws://testproducer:8080')

async def receive_websocket(topic):
    session = aiohttp.ClientSession()
    async with session.ws_connect(URL) as ws:
        async for msg in ws:
            print('> ', msg)

            if msg.type in (aiohttp.WSMsgType.CLOSED,
                            aiohttp.WSMsgType.ERROR):
                break

            await topic.send(value=msg.data)

if __name__ == '__main__':
    while True:
        try:
            app = faust.App(TOPIC, broker=BROKER)
            topic = app.topic(TOPIC, value_type=BROKER)
            app.finalize()

            loop = asyncio.get_event_loop()
            loop.run_until_complete(receive_websocket(topic))
            loop.run_forever()

        except:
            logging.error(traceback.format_exc())
            time.sleep(1)
            continue
