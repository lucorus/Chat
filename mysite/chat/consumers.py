import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime


class ChatConsumer(AsyncWebsocketConsumer):
    # Пользователь присоединился к чату (отправляем сообщение об этом)
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_send(self.room_group_name,{"type": "chat.message", "message": 'user connect'})
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    # Пользователь вышел из чата
    async def disconnect(self, close_code):
        await self.channel_layer.group_send(self.room_group_name,{"type": "chat.message", "message": 'user disconnect'})
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Отправляем сообщение в текущую группу
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        current_time = datetime.now().strftime("%H:%M:%S")
        message_with_time = f"{current_time}: {message}"

        await self.channel_layer.group_send(self.room_group_name, {"type": "chat.message", "message": message_with_time})

    # Получаем сообщение
    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))