from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing, Bid, User, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import ListingForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

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

class ListingCreateView(LoginRequiredMixin, CreateView):
	login_url = '/members/'
	form_class = ListingForm
	model = Listing
	# fields = '__all__'
	success_url = reverse_lazy('home')

class ListingDetailView(DetailView):
	model = Listing

def toggle_watchlist(request, pk):
	# pass
	listing = get_object_or_404(Listing, pk=pk)
	if request.user.watchlist.filter(id=pk).exists():
		request.user.watchlist.remove(listing)
	else: 
		request.user.watchlist.add(listing)
	return HttpResponseRedirect(reverse('listing-detail', args=[str(pk)]))



# 	post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     like = False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)
#         like = True
#     return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))