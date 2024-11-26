from django import forms 
from .models import *


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['business_name', 'business_location', 'NID']  

