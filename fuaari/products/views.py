from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductsForms
from seller.models import Seller  
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def create_product(request, seller_id):
    seller = get_object_or_404(Seller, pk=seller_id)
    if request.method == 'POST':
        form = ProductsForms(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller_id = seller  
            product.save()
            return redirect('product_list')  
    else:
        form = ProductsForms()
    
    context = {
        'form': form,
        'seller': seller,
    }
    return render(request, 'products/create_product.html', context)

@login_required
def delete_product(request, product_id):
    Products.objects.get(pk=product_id).delete()
    return redirect('product_list')
   
def product_list(request):
    products = Products.objects.all()
    return render(request, 'products/product_list.html', {'product': products})    

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        form = ProductsForms(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form = ProductsForms(instance=product)

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/edit_product.html', context)
