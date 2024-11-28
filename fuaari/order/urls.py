from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:product_id>/<int:buyer_id>/', views.create_order, name='create_order'),
]
