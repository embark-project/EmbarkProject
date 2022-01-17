from django.db import models 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
# Create your models here.

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,100)]

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
    product = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
   
    class Meta:
      db_table = "Req"
      

    def __str__(self):
        return f'Posted {self.quantity} {self.product} under {self.category} '

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=40)
    product = models.CharField(max_length=20)
    quantity = models.IntegerField(choices=INTEGER_CHOICES)
    price= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    approved_status = models.IntegerField(default=0) 
    reason = models.CharField(max_length=70)

    def __str__(self):
        return f'Need {self.quantity} {self.product} under {self.category}.The determined price is {self.price}'


   

     

