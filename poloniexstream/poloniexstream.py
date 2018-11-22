#!/usr/bin/env python
import traceback
import logging
import asyncio
import aiohttp
import faust
import os
import time
import json

TOPIC = os.getenv('TOPIC', 'poloniex')
BROKER = os.getenv('BROKER', 'kafka://kafka:9092')
URL = os.getenv('URL', 'wss://api2.poloniex.com')

channels = {
    'HEARTBEAT': 1010,
    'TICK_ALL_CURRENCIES': 1002,
    'USDT_BTC': 121,
    'USDT_DOGE': 216,
    'USDT_DASH': 122,
    'USDT_LTC': 123,
    'USDT_NXT': 124,
    'USDT_STR': 125,
    'USDT_XMR': 126,
    'USDT_XRP': 127,
    'USDT_ETH': 149,
    'USDT_SC': 219,
    'USDT_LSK': 218,
    'USDT_ETC': 173,
    'USDT_REP': 175,
    'USDT_ZEC': 180,
    'USDT_GNT': 217,
    'USDT_BCH': 191,
    'USDT_ZRX': 220,
    'USDT_EOS': 203,
    'USDT_SNT': 206,
    'USDT_KNC': 209,
    'USDT_BAT': 212,
    'USDT_LOOM': 215,
    'USDT_QTUM': 223
}

async def receive_websocket():
    session = aiohttp.ClientSession()
    async with session.ws_connect(URL) as ws:
        for channel, id in channels.items():
            sub_msg = {"command": "subscribe", "channel": id}
            await ws.send_str(json.dumps(sub_msg))

        async for msg in ws:
            #print('> ', msg)
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
            loop.run_until_complete(receive_websocket())
            loop.run_forever()

        except:
            logging.error(traceback.format_exc())
            time.sleep(1)
            continue
