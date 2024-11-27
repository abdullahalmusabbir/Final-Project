from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=('buyer_id','product_id','rating','comment')
    search_fields=('buyer_id','product_id')
