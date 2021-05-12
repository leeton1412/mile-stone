from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """Simple View to show all products"""
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, "products/products.html", context)

def detail(request, product_id):
    """Show Products Details"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "products/detail.html", context)

