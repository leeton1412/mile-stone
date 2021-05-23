from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


def profiles(request):
    """Simple View to render page"""
    return render(request, "profiles/profiles.html")