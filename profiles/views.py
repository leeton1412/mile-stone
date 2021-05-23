from django.shortcuts import render, get_object_or_404
from .models import UserProfile
# Create your views here.


def profiles(request):
    """Simple View to render page and display profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profiles.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)