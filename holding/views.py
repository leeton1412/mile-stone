from django.shortcuts import render

# Create your views here.


def bag_view(request):
    """Simple View to render page"""
    return render(request, "holding/shopping-bag.html")
