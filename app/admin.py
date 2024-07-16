from django.contrib import admin
from .models import Chat,Group,Notification
# Register your models here.

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display=['message_date','thread_name','group','message']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display=['group_name']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=['chat','owner','is_seen']