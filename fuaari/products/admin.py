from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','avaibility','category','price','images')
    search_fields = ('name','price')
