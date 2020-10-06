from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing, Bid, User, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import ListingForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Max, Count
from django import forms

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
	return render(request, 'auctions/categories.html', {'categories': categories, 'request': request})

def category_listings(request, category):
	listings_by_category = Listing.objects.filter(category=category.upper())
	return render(request, 'auctions/listing_list.html', {'listing_list': listings_by_category})

class ListingCreateView(LoginRequiredMixin, CreateView):
	login_url = '/members/'
	form_class = ListingForm
	model = Listing
	success_url = reverse_lazy('home')


def listing_detail(request, pk):
	listing = get_object_or_404(Listing, pk=pk)
	comments_list = Comment.objects.all()
	comment_form = CommentForm()
	watching = False
	if request.user.is_authenticated:
		if request.user.watchlist.filter(id=pk).exists():
			watching = True
	return render(request, 'auctions/listing_detail.html', {
		'listing': listing, 
		'watching': watching, 
		'comment_form':comment_form,
		'comments_list':comments_list
	})
# class ListingDetailView(DetailView):
# 	model = Listing

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(** kwargs)
# 		watching = False
# 		comments_list = Comment.objects.all()
# 		# can get the request through self.request
# 		if self.request.user.is_authenticated:
# 			if self.request.user.watchlist.filter(id=self.kwargs['pk']).exists():
# 				watching = True
# 		context['watching'] = watching
# 		context['comment_form'] = CommentForm()
# 		context['comments_list'] = comments_list
# 		return context

@login_required(login_url='/members/')
def add_comment(request, pk):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		listing = get_object_or_404(Listing, pk=pk)

		if form.is_valid():
			comment = form.cleaned_data['comment']
			title = form.cleaned_data['title']
			comment = Comment(listing=listing, comment=comment, title=title, commenter=request.user)
			comment.save()
		return HttpResponseRedirect(reverse('listing-detail', args=(listing.id,)))

@login_required(login_url='/members/')
def toggle_watchlist(request, pk):
	# pass
	listing = get_object_or_404(Listing, pk=pk)
	if request.user.watchlist.filter(id=pk).exists():
		request.user.watchlist.remove(listing)
	else: 
		request.user.watchlist.add(listing)
	return HttpResponseRedirect(reverse('listing-detail', args=[str(pk)]))

@login_required(login_url='/members/')
def toggle_watchlist_home(request, pk):
	# pass
	listing = get_object_or_404(Listing, pk=pk)
	if request.user.watchlist.filter(id=pk).exists():
		request.user.watchlist.remove(listing)
	else: 
		request.user.watchlist.add(listing)
	return HttpResponseRedirect(reverse('listings'))

@login_required(login_url='/members/')
def watchlist(request):
	watchlist = request.user.watchlist.all()

	return render(request, 'auctions/listing_list.html', {'listing_list':watchlist})

def search(request):
	if request.method == 'POST':
		search_term = request.POST["search"]
		searched_listings = Listing.objects.filter(title__contains=search_term)

		return render(request, 'auctions/listing_list.html', {'listing_list': searched_listings})