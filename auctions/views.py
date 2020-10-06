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
	return render(request, 'auctions/categories.html', {'categories': categories, 'request': request})

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
	def get_context_data(self, **kwargs):
		context = super().get_context_data(** kwargs)
		watching = False
		comments_list = Comment.objects.all()
		# can get the request through self.request
		if self.request.user.is_authenticated:
			if self.request.user.watchlist.filter(id=self.kwargs['pk']).exists():
				watching = True
		context['watching'] = watching
		context['comment_form'] = CommentForm()
		context['comments_list'] = comments_list
		return context

def add_comment(request, pk):

	form = CommentForm(request.POST)
	listing = get_object_or_404(Listing, pk=pk)

	if form.is_valid():
		comment = form.cleaned_data['comment']
		title = form.cleaned_data['title']
		comment = Comment(comment=comment, title=title, commenter=request.user)
		comment.save()
		return HttpResponseRedirect(reverse('listing', args=(listing.id,)))

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

@login_required(login_url='/members/')
def add_comment(request):
	form = forms.ModelForm(request.POST)