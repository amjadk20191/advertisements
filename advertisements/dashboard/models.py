from django.db import models
from django.core.validators import  MinValueValidator

class plan(models.Model):

    name=models.CharField(max_length=50)
    number_of_day=models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2,validators=[MinValueValidator(0)])
