from django import forms
from .models import Listing, Bid, Comment
from django.core.exceptions import ValidationError

class BidForm(forms.ModelForm):
    class Meta: 
        model = Bid
        fields = ['bid_price']
        widgets = {
            'bid_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bid'})
        }
    def __init__(self, *args, **kwargs):
        # Add listing from the second argument passed in
        self.listing = kwargs.pop('listing', None)
        super(BidForm, self).__init__(*args, **kwargs)
        self.fields['bid_price'].label = ''
    
    # validation for bid price 
    def clean_bid_price(self):
        bid_price = self.cleaned_data['bid_price']
        bids = Bid.objects.filter(listing=self.listing)
        if bids:
            highest_bid_price = bids.order_by('bid_price').last().bid_price
            if bid_price <= highest_bid_price:
                raise ValidationError('Bid must be greater than any bids already placed.')
        else:
            if bid_price < self.listing.price:
                raise ValidationError('Bid must be as large as the starting price.')

        return bid_price


class ListingForm(forms.ModelForm):

    class Meta: 
        model = Listing
        fields = ('title', 'price', 'image', 'category', 'creator', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'image': forms.URLInput(attrs={'class': 'form-control mb-2'}),
            'category': forms.Select(attrs={'class': 'form-control mb-2'}),
            'creator': forms.Select(attrs={'class': 'form-control mb-2'}),
            # 'active': forms.CheckboxInput(attrs={'class': 'largerCheckbox mb-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-2', 'maxlength': '600'}),
            # 'winner': forms.Select(attrs={'class': 'form-control mb-2'}),
            'creator': forms.TextInput(attrs={'class': 'form-control mb-2', 'id':'creator', 'type':'hidden', 'value': ''}),
        }

    # Remove comment for no labels
    # def __init__(self, *args, **kwargs):
    #     super(ListingForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].label = ''
    #     self.fields['price'].label = ''
    #     self.fields['image'].label = ''
    #     self.fields['category'].label = ''
    #     self.fields['active'].label = ''
    #     self.fields['description'].label = ''
    #     self.fields['winner'].label = ''

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('title', 'comment')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment'})
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['comment'].label = ''