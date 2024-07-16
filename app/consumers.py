from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import json
from channels.layers import get_channel_layer
from .models import *
from channels.db import database_sync_to_async
# from django.contrib.auth.models import User
from django.utils import timezone


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('websocket connected..!')
        self.group_name=self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()

    async def receive(self,text_data=None,bytes_data=None):
        
        new_message=json.loads(text_data)
        print('new_message',new_message)
        group=await database_sync_to_async(Group.objects.get)(group_name=self.group_name)
        if self.scope['user'].is_authenticated:
            self.user=self.scope["user"]
           
            
            chat=await database_sync_to_async(Chat.objects.create)(group=group,message=new_message['msg'],owner=self.user)
            # new_message['user']=self.user.username
            # new_message['message_date']=chat.message_date

            await self.channel_layer.group_send(self.group_name,{
            'type':'chat.message',
            'message':new_message['msg'],
            'message_date':new_message['message_date'],
            'user':new_message['user'],
            'user_photo':new_message['user_photo']
            

            })
    async def chat_message(self,event):

        message=json.dumps(event)
        await self.send(text_data=message)

        
        

    async def disconnect(self,close_code):
        print('websocket disconnected .. !')
        await self.channel_layer.group_discard(self.group_name,self.channel_name)



class AsyncPersonChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('websocket connected ..')
        if (self.scope['user'].is_authenticated):
            self.self_user_id=self.scope['user'].id
        self.other_user_id=self.scope['url_route']['kwargs']['id']
        if (self.self_user_id > self.other_user_id):
            self.group_name=f'chat_{self.self_user_id}-{self.other_user_id}'
        else:
            self.group_name=f'chat_{self.other_user_id}-{self.self_user_id}'
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()
       

    async def receive(self,text_data=None,bytes_data=None):
        data=json.loads(text_data)
        
        
        chat=await database_sync_to_async(Chat.objects.create)(group=None,thread_name=self.group_name,message=data['msg'],owner=self.scope['user'])
        getuser=await database_sync_to_async(MyUser.objects.get)(id=self.other_user_id)
        await database_sync_to_async(Notification.objects.create)(chat=chat,owner=getuser)
        await self.channel_layer.group_send(self.group_name,{
            'type':'chat.message',
            'message':data['msg'],
            'message_date':data['message_date'],
            'user':data['user'],
            'user_photo':data['user_photo']
            
            })
    async def chat_message(self,event):
        data=json.dumps(event)
        await self.send(text_data=data)
    async def disconnect(self,close_code):
        print('websocket disconnected ..!')
        await self.channel_layer.group_discard(self.group_name,self.channel_name)       

class AsyncOnlineConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        self.group_name='user'
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()
    async def receive(self,text_data=None,bytes_data=None):
        data=json.loads(text_data)

        user=await database_sync_to_async(MyUser.objects.get)(username=data['user'])

        if (data['status'] == 'open'):
            user.status_online=True
            await database_sync_to_async(user.save)()
        else:
            user.status_online=False
            await database_sync_to_async(user.save)()
        print(data)
        await self.channel_layer.group_send(self.group_name,{
        'type':'chat.message',
        'user':data['user'],
        'status':data['status']
        })
    async def chat_message(self,event):
        data=json.dumps(event)
        await self.send(text_data=data)
    async def disconnect(self,close_code):
        print('websocket disconnected..')
        await self.channel_layer.group_discard(self.group_name,self.channel_name)

class SendNotification(AsyncWebsocketConsumer):
    async def connect(self):
        print('websocket connected')
        myid=self.scope['user'].id
        self.group_name=f'{myid}'
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()

    async def send_notification(self,event):
        data=json.loads(event['value'])
        print(data)
        await self.send(text_data=json.dumps(data))
    async def disconnect(self,close_code):
        print('websocket disconnected')
        await self.channel_layer.group_discard(self.group_name,self.channel_name)