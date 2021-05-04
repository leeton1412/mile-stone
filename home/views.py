from django.shortcuts import render

# Create your views here.


def index(request):
    """Simple View to render page"""
    return render(request, "home/index.html")
