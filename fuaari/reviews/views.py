from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewsForm
from products.models import Products
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from orders.models import Order

@login_required
def create_reviews(request, product_id,buyer_id):
    product = get_object_or_404(Products, id=product_id)
    buyer=get_object_or_404(User, id=buyer_id)
    # buyer = request.user  # Assuming the buyer is the logged-in user
    
    # has_purchased = Order.objects.filter(user=request.user, product_id=product.id).exists()

    # if not has_purchased:
    #     messages.error(request, "You cannot review a product you haven't purchased.")
    #     return redirect('product_list')  # Redirect to product list or another appropriate page

    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.buyer_id = buyer  
            review.product_id = product 
            review.save()
            return redirect('product_list')  
    else:
        form = ReviewsForm()

    return render(request, 'reviews/create_reviews.html', {'form': form, 'product': product})
