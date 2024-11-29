from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SellerForm, ProfileForm
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from functools import wraps
from products.models import *

def seller_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, 'seller'):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    return _wrapped_view

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        is_seller = request.POST.get('is_seller') == 'on'

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

            Profile.objects.create(user=user, phone_number=phone_number)

            if is_seller:
                seller_form = SellerForm(request.POST)
                if seller_form.is_valid():
                    seller = seller_form.save(commit=False)
                    seller.user = user
                    seller.save()
                    messages.success(request, "Seller account created successfully!")
                    return redirect('login')
                else:
                    user.delete()  
                    messages.error(request, "Failed to create seller account. Please check the form.")
                    return redirect('signup')  
            else:
                messages.success(request, "User account created successfully!")

            return redirect('product_list')  

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('signup')  

    else:
        seller_form = SellerForm()
        profile_form = ProfileForm()
        return render(request, 'seller/create_seller.html', {'seller_form': seller_form, 'profile_form': profile_form})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('product_list')  
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('log_in')  

    return render(request, 'seller/login.html')  

@login_required
def sign_out(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login')  

@login_required
@seller_required
def deshboard(request):
    products = Products.objects.all()
    return render(request,'seller/deshseller.html',{'products': products})
