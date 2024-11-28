from django import forms 
from .models import *

class ProductsForms(forms.ModelForm):
    class Meta:
        model=Products
        fields=['name','description','avaibility','price','images']
