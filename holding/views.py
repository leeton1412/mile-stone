from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product
# Create your views here.

def bag_view(request):
    """Simple View to render page"""
    return render(request, "holding/shopping-bag.html")

def add_item(request, item_id):
    """ View to add items to bag """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('amount'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Amount of {product.name} updated to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_item(request, item_id):
    """ View to update items in bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('amount'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Amount of {product.name} updated to {bag[item_id]}')
    else:
        bag.pop[item_id]
        messages.success(request, f'Amount of {product.name} updated to {bag[item_id]}')

    request.session['bag'] = bag
    return redirect(reverse('bag_view'))


def remove_item(request, item_id):
    """ View to clear bag """
    
    try:
        product = Product.objects.get(pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop[item_id]
        messages.success(request, f'{product.name} removed')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
        
