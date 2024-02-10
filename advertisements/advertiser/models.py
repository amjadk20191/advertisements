from django.db import models
from core.models import upload_path
from core.models import User
# Create your models here.
from django.core.validators import  MinValueValidator
from rest_framework.exceptions import APIException

import os

class advertisement(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    country=models.CharField( max_length=30)
    description=models.TextField()
    URL=models.URLField()
    image=models.ImageField(upload_to=upload_path, blank=True, null=True)
    cative=models.BooleanField(blank=True, null=True)
    active_to_see=models.BooleanField(blank=True, default=False)
    important=models.DecimalField(blank=True,null=True,max_digits=30,decimal_places=15)
    important_group=models.PositiveSmallIntegerField(default=0)
    refuse_text=models.TextField(blank=True, null=True)
    date_of_end=models.DateField()
    date_of_start=models.DateField()
    price = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True,validators=[MinValueValidator(0)])
   

   

   
   
    def delete(self, *args, **kwargs):
        try:
           image_path = self.image.path
           if os.path.exists(image_path):
               os.remove(image_path)
        except:
            pass

        
        return super().delete(*args, **kwargs)
        



class seen_advertisement(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    advertisement = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'advertisement')
   

    