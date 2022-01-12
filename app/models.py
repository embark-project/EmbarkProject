from django.db import models 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
# Create your models here.

class User_type(AbstractUser):
    address = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length=15,null=True)
   
    class Meta:
      db_table = "User_type"
      

    def __str__(self):
        return f'{self.username} registered as {self.role} '
  

class Req(models.Model):
    category = models.CharField(max_length=40)
    product = models.CharField(max_length=10)
   
    class Meta:
      db_table = "Req"
      

    def __str__(self):
        return f'Posted {self.product} under {self.category} '

class Order(models.Model):
    category = models.CharField(max_length=40)
    product = models.CharField(max_length=10)
    is_approved = models.BooleanField(default=False) #hide



    def __str__(self):
        return f'Need {self.product} under {self.category} '

    @property
    def approve_leave(self):
        if not self.is_approved:
            self.is_approved = True
            self.status = 'approved'
            self.save()

    @property
    def decline(self):
        if self.is_approved or not self.is_approved:
            self.is_approved = False
            self.status = 'declined'
            self.save()
 


   

     

