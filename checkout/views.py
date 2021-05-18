from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from holding.contexts import bag_contents
from .forms import OrderForm

import stripe


# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Nothing here to munch on!")
        return redirect(reverse('products'))

    this_bag = bag_contents(request)
    total = this_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    
    order_form = OrderForm()

    if not stripe_public_key:
        messages.error(request, 'Stripe Public Key Missing, Check Variables')
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
