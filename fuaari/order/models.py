from django.db import models

# Create your models here.
class Order(models.Model):
    quantity=models.IntegerField()
    order_date=models.DateTimeField(auto_now_add=True)
    buyer_id=models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE, related_name='order')
    address=models.TextField()
    price=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='orders')
