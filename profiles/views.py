from django.shortcuts import render

# Create your views here.

def profiles(request):
    """Simple View to render page"""
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)