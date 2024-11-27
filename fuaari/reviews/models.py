from django.db import models
from users.models import *
from products.models import *

# Create your models here.
class Review(models.Model):
    buyer_id=models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product_id=models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
    rating=models.IntegerField()
    comment=models.CharField(max_length=225)
    
    
