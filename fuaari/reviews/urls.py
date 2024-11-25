from django.urls import path
from . import views

urlpatterns = [
    path('create_reviews/',views.create_reviews,name='create_reviews')
]


