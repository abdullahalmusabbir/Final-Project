from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from products.models import Products
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_order(request, product_id,buyer_id):
    product = get_object_or_404(Products, pk=product_id)
    buyer = get_object_or_404(User, pk=buyer_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product_id = product
            order.buyer_id = buyer
            order.price = product  
            order.save()
            return redirect('product_list')  
    else:
        form = OrderForm()
    
    context = {
        'form': form,
        'product': product,
        'buyer': buyer,
    }
    return render(request, 'orders/create_order.html', context)
