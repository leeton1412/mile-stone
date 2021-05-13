from django.shortcuts import render, redirect

# Create your views here.


def bag_view(request):
    """Simple View to render page"""
    return render(request, "holding/shopping-bag.html")

def add_item(request, item_id):
    """ View to add items to bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)