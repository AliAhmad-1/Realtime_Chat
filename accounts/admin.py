from django.contrib import admin
from .models import MyUser
# Register your models here.
@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','email','photo']

