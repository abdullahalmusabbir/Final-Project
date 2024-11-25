from django.urls import path
from . import views

urlpatterns = [
    path('create_product/<int:seller_id>/', views.create_product, name='create_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product_list/',views.productlist,name='product_list'),
]

