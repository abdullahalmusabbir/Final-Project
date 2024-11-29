
from django import forms 
from .models import *

class ReviewsForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['rating','comment']
