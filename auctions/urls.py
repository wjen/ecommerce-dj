from django.urls import path
from . import views
from .views import ListingListView, ListingListViewByActive, categories, ListingCreateView, toggle_watchlist, toggle_watchlist_home, watchlist, add_comment
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='listings/', permanent=True), name='home'),
    # path('', views.index, name='index'),
    path('listings/', ListingListView.as_view(), name='listings'),
    path('listings/active', ListingListViewByActive.as_view(), name='listings-active'),
    path('lstings/create', ListingCreateView.as_view(), name='listing-create'),
    path('listing/<int:pk>', views.listing_detail, name='listing-detail'),
    path('listing/<int:pk>/add_comment', views.add_comment, name='add-comment'),
    path('categories', views.categories, name='categories'),
    path('categories/<str:category>', views.category_listings, name='category-listings'),
    path('toggle_watchlist/<int:pk>', views.toggle_watchlist, name='toggle-watchlist'),
    path('toggle_watchlist_home/<int:pk>', views.toggle_watchlist_home, name='toggle-watchlist-home'),
    path('watchlist', views.watchlist, name='watchlist'),
]
