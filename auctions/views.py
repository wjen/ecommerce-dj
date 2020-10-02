from django.shortcuts import render, redirect
from .models import Listing, Bid, User, Comment
# Create your views here.
def index(request):

    return render(request, 'index.html', {})