from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Nothing here to munch on!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IsXGOEXwwcaVeHN4rPgTtOGN5S3PdqHcePqQ5QMHNeLoYcvTVnMopxSVsQoWOX6S55WJoEj3cBRK7EGWqABn2iG00b2KU7SDZ',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
