import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from notice.serializers import SignalAlertSerializer
from channels.layers import get_channel_layer


class SignalsAlertWS(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_group_name = 'signals'
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data = text_data_json['data']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_alert',
                'data': data
            }
        )

    # Receive message from room group
    async def send_alert(self, event):
        data = event['data']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({'data': data}))

    async def sendNewSignalAlert(signal):
        room_name = 'signals'
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(room_name, {
            'type': 'send_alert',
            'data': SignalAlertSerializer(data=signal),
        })
        pass


class ArticlesWS(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'articles'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
