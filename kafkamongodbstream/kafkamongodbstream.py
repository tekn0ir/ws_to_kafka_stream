#!/usr/bin/env python
import faust
import os
import motor.motor_asyncio

TOPIC = os.getenv('TOPIC', 'test')
BROKER = os.getenv('BROKER', 'kafka://kafka:9092')
# MONGO_URL = os.getenv('MONGO_URL', 'mongodb://root:example@mongodb:27017')
# MONGO_DB = os.getenv('MONGO_DB', 'database')
# MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'collection')

app = faust.App(TOPIC, broker=BROKER)
topic = app.topic(TOPIC, value_type=str)
# mongodb = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
# db = mongodb[MONGO_DB]

@app.agent(topic)
async def process_topic(messages):
    async for msg in messages:
        print('> ', msg)
        #result = await db[MONGO_COLLECTION].insert_one(msg)
        #print('result %s' % repr(result.inserted_id))

if __name__ == '__main__':
    app.main()
