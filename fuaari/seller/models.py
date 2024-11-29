from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    business_name = models.CharField(max_length=255)
    business_location = models.TextField()
    NID = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.business_name} ({self.user.username})"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    purchased_products = models.JSONField(default=list)

    def __str__(self):
        return self.user.username    
