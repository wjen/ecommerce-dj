from django.db import models
from django.contrib.auth.models import AbstractUser
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing', blank=True, related_name='watchlist')

class Listing(models.Model):
    LISTING_CATEGORIES = [
        ('BOOKS', 'Books'),
        ('MUSIC', 'Music'),
        ('MOVIES', 'Movies'),
        ('GAMES', 'Games'),
        ('ELECTRONICS', 'Electronics'),
        ('KITCHEN', 'Kitchen'),
        ('BABY', 'Baby'),
        ('TRAVEL', 'Travel'),
        ('CLOTHING', 'Clothes'),
        ('ANIMALS', 'Animals'),
        ('SPORTS', 'Sports'),
        ('FOOD', 'Food')
    ]
    title = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.URLField(blank=True, verbose_name='Image URL', null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings', null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    category = models.CharField(max_length=16, choices=LISTING_CATEGORIES)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Returns the url to access a detail record for thislisting.
        return reverse('listing-detail', args=[str(self.id)])

class Bid(models.Model):
    bid_price = models.DecimalField(decimal_places=2, max_digits=10)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    timestamp = models.DateTimeField(auto_now_add=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='placed_bids')

    def __str__(self):
        return f'{self.bidder} placed bid of ${self.bid_price} for {self.listing}'

class Comment(models.Model):
    title = models.CharField(max_length=155, blank=True)
    comment = models.CharField(max_length=600, blank=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.commenter} - {self.comment} ({self.timestamp.date()})'
