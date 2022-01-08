from django.db import models 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User_type(AbstractUser):
    address = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length=15,null=True)
   
    class Meta:
      db_table = "User_type"
      

    def __str__(self):
        return f'{self.username} registered as {self.role} '
  


