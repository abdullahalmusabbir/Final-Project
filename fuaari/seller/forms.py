from django import forms
from .models import Seller, Profile

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['business_name', 'business_location', 'NID']
        widgets = {
            'business_name': forms.TextInput(attrs={'placeholder': 'Enter business name'}),
            'business_location': forms.Textarea(attrs={'placeholder': 'Enter business location', 'rows': 3}),
            'NID': forms.TextInput(attrs={'placeholder': 'Enter NID'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        }
