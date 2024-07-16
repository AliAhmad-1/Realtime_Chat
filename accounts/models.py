from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    username=models.CharField(max_length=250,unique=True,blank=True)
    photo=models.ImageField(upload_to='user_photos/',blank=True,null=True)
    status_online=models.BooleanField(default=False)
    

    def __str__(self):
        return self.username


