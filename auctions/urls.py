from django.urls import path
from . import views
from .views import ListingListView, ListingListViewByActive, categories, ListingCreateView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='listings/', permanent=True), name='home'),
    # path('', views.index, name='index'),
    path('listings/', ListingListView.as_view(), name='listings'),
    path('listings/active', ListingListViewByActive.as_view(), name='listings-active'),
    path('lstings/create', ListingCreateView.as_view(), name='listing-create'),
    path('categories', views.categories, name='categories'),
    path('categories/<str:category>', views.category_listings, name='category-listings')
]
