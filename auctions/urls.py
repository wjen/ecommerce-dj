from django.urls import path
from . import views
from .views import ListingListView, ListingListViewByActive, ListingCreateView, ListingUpdateView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='listings/', permanent=True), name='home'),
    path('listings/', ListingListView.as_view(), name='listings'),
    path('listings/active', ListingListViewByActive.as_view(), name='listings-active'),
    path('lstings/create', ListingCreateView.as_view(), name='listing-create'),
    path('listing/<int:pk>', views.listing_detail, name='listing-detail'),
    path('listing/<int:pk>/add_comment', views.add_comment, name='add-comment'),
    path('listing/<int:pk>/add_bid', views.add_bid, name='add-bid'),
    path('listing/<int:pk>/delete_listing', views.delete_listing, name='delete-listing'),
    path('listings/<int:pk>/update_listing', views.ListingUpdateView.as_view(), name='update-listing'),
    path('categories', views.categories, name='categories'),
    path('categories/<str:category>', views.category_listings, name='category-listings'),
    path('toggle_watchlist/<int:pk>', views.toggle_watchlist, name='toggle-watchlist'),
    path('toggle_watchlist_home/<int:pk>', views.toggle_watchlist_home, name='toggle-watchlist-home'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('search', views.search, name='search'),
]
