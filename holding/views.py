from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products import Product
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
    else:
        bag[item_id] = quantity

    messages.success(request, f'Added {product.name} to your bag')
    request.session['bag'] = bag
    return redirect(redirect_url)


def update_item(request, item_id):
    """ View to update items in bag """

    quantity = int(request.POST.get('amount'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('bag_view'))


def remove_item(request, item_id):
    """ View to clear bag """
    try:
        bag = request.session.get('bag', {})

        bag.pop[item_id]

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
        
