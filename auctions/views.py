from django.shortcuts import render, redirect
from .models import Listing, Bid, User, Comment
# Create your views here.
def index(request):
    listing_list = Listing.objects.filter(active=True)
    return render(request, 'index.html', {'listing_list': listing_list})

