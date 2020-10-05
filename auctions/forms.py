from django import forms
from .models import Listing, Bid, Comment

class ListingForm(forms.ModelForm):

    class Meta: 
        model = Listing
        fields = ('title', 'price', 'image', 'category', 'creator', 'active', 'description', 'winner')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.URLInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'creator': forms.Select(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'largerCheckbox'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'maxlength': '600'}),
            'winner': forms.Select(attrs={'class': 'form-control'}),
            'creator': forms.TextInput(attrs={'class': 'form-control', 'id':'creator', 'type':'hidden', 'value': ''}),
        }
    # def __init__(self, *args, **kwargs):
    #     super(ListingForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].label = ''
    #     self.fields['price'].label = ''
    #     self.fields['image'].label = ''
    #     self.fields['category'].label = ''
    #     self.fields['active'].label = ''
    #     self.fields['description'].label = ''
    #     self.fields['winner'].label = ''

#     LISTING_CATEGORIES = [
#         ('BOOKS', 'Books'),
#         ('MUSIC', 'Music'),
#         ('MOVIES', 'Movies'),
#         ('GAMES', 'Games'),
#         ('ELECTRONICS', 'Electronics'),
#         ('KITCHEN', 'Kitchen'),
#         ('BABY', 'Baby'),
#         ('TRAVEL', 'Travel'),
#         ('CLOTHING', 'Clothes'),
#         ('ANIMALS', 'Animals'),
#         ('SPORTS', 'Sports'),
#         ('FOOD', 'Food')
#     ]
#     title = models.CharField(max_length=200)
#     price = models.DecimalField(decimal_places=2, max_digits=10)
#     image = models.URLField(blank=True, verbose_name='Image URL', null=True)
#     creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings', null=True)
#     active = models.BooleanField(default=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     description = models.TextField()
#     category = models.CharField(max_length=16, choices=LISTING_CATEGORIES)
#     winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'title_tag', 'author',
#                   'category', 'body', 'snippet', 'header_image')
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'elder', 'value': '', 'type': 'hidden'}),
#             'snippet': forms.Textarea(attrs={'class': 'form-control'}),
#             # 'author': forms.Select(attrs={'class': 'form-control'}),
#             'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
#         }