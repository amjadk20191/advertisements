from django.db import models

# Create your models here.

class complaints(models.Model):

    
    description=models.TextField()
    email=models.EmailField(blank=True,null=True)
    phone=models.CharField(max_length=17,blank=True,null=True)
   

class connect_with_us(models.Model):

    
    description=models.TextField()
    email=models.EmailField(blank=True,null=True)
    phone=models.CharField(max_length=17,blank=True,null=True)
   
class opinion(models.Model):

    
    description=models.TextField()
    active=models.BooleanField(default=False,blank=True)
   