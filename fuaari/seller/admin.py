from django.contrib import admin
from .models import *

class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'business_name', 'business_location', 'NID', 'get_phone_number')
    search_fields = ('user__username', 'business_name', 'NID')
    list_filter = ('business_location',)

    def get_phone_number(self, obj):
        return obj.user.profile.phone_number if hasattr(obj.user, 'profile') else "N/A"
    get_phone_number.short_description = 'Phone Number'

admin.site.register(Seller, SellerAdmin)
admin.site.register(Profile)  
