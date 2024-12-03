from django.db import models
from seller.models import Seller

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=225)
    description=models.CharField(max_length=1024)
    avaibility=models.IntegerField()
    price=models.FloatField()
    images=models.ImageField(upload_to='photos/')
    seller_id=models.ForeignKey(Seller,on_delete=models.CASCADE, related_name='products')
    category = models.CharField(max_length=100, blank=True, null=True)
