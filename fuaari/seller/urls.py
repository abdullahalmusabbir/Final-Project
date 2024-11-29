from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.log_in,name='login'),
    path('signout/',views.sign_out,name='signout'),
    path('deshboard/',views.deshboard,name='deshboard'),
]
