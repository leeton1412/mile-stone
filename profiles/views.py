from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
# Create your views here.


def profiles(request):
    """Simple View to render page and display profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)