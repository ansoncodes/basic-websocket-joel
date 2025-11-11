# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Client connected!")
        await self.accept() 

    async def disconnect(self, close_code):
        print("Client disconnected!")

    async def receive(self, text_data):
        print("Received:", text_data)
        data = json.loads(text_data)
        message = data.get('message', '')
        await self.send(text_data=json.dumps({
            'message': f'Server received: {message}'
        }))
