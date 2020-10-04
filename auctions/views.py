from django.shortcuts import render, redirect
from .models import Listing, Bid, User, Comment
from django.views.generic import ListView
# Create your views here.
# def index(request):
#     listing_list = Listing.objects.all()
#     return render(request, 'index.html', {'listing_list': listing_list, 'page': 'All Listings'})

class ListingListView(ListView):
	model = Listing
	paginate_by = 12

class ListingListViewByActive(ListView):
	model = Listing
	paginate_by = 12
	template_name='auctions/listing_list.html'

	def get_queryset(self):
		return Listing.objects.filter(active=True)

def categories(request):
	# categories = Listing.objects.filter(active=True).order_by('category')
	categories = Listing.objects.filter(active=True).order_by("category").values_list('category', flat=True).distinct()
	categories = [category.capitalize() for category in categories]
	return render(request, 'auctions/categories.html', {'categories': categories})

def category_listings(request, category):
	listings_by_category = Listing.objects.filter(category=category.upper())
	return render(request, 'auctions/listing_list.html', {'listing_list': listings_by_category})