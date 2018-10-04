#!/bin/env python

import asyncio
import datetime
import time
import random
import websockets
import os
import math
import uuid
import sys

HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 8080))

names = ["pew", "mew", "dew", "few", "new", "sew"]
metrics = {}
for metric in names:
    metrics[metric] = 0.0

def random_walk(metric):
    metrics[metric] += math.sin((random.randint(0, 9999)/10000.0) * math.pi * 2.0)
    return metrics[metric]

async def loop(websocket, path):
    while True:
        for metric in names:
            message = {"datetime": datetime.datetime.utcnow().isoformat() + 'Z', "time": int(round(time.time() * 1000)), "name": "metric." + metric, "value": random_walk(metric), "dimensions": { "id": str(uuid.uuid4()) }}
            print(message)
            await websocket.send(f"{message}")
        sys.stdout.flush()
        await asyncio.sleep(0.1)

start_server = websockets.serve(loop, HOST, PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
