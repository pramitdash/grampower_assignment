import imp
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep
from random import randint

class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        for i in range(1000):
            await self.send(json.dumps({"value": randint(1, 20)}))
            await sleep(1)