import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer



class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "staffs"
    
        await self.accept()
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(data)
     

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_message_to_frontend",
                "message": data,
              
            },
        )

    async def send_message_to_frontend(self, event):
        await self.send(text_data=json.dumps(event))


