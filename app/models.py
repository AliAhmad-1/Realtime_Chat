from django.db import models
from django.contrib.auth.models import User
from accounts.models import MyUser
# Create your models here.

class Chat(models.Model):
    message=models.CharField(max_length=255)
    owner=models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='user_messages')
    message_date=models.DateTimeField(auto_now=True)
    thread_name=models.CharField(max_length=50,null=True,blank=True)
    group=models.ForeignKey('Group',on_delete=models.CASCADE,related_name='group_messages',null=True)

    def __str__(self):
        return f'{self.owner.username}:{self.message}'

class Group(models.Model):
    group_name=models.CharField(max_length=150,unique=True)


    def __str__(self):
        return self.group_name


class Notification(models.Model):
    chat=models.ForeignKey(Chat,on_delete=models.CASCADE,related_name='chat_notifi')
    owner=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    is_seen=models.BooleanField(default=False)
