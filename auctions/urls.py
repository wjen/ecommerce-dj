from django.urls import path
from . import views
from .views import ListingListView, ListingListViewByActive, categories
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='listings/', permanent=True), name='home'),
    # path('', views.index, name='index'),
    path('listings/', ListingListView.as_view(), name='listings'),
    path('listings/active', ListingListViewByActive.as_view(), name='listings_active'),
    path('categories', views.categories, name='categories'),
    path('categories/<str:category>', views.category_listings, name='category_listings')
]
