from django import forms
from .models import Listing, Bid, Comment

class ListingForm(forms.ModelForm):

    class Meta: 
        model = Listing
        fields = ('title', 'price', 'image', 'category', 'creator', 'active', 'description', 'winner')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'image': forms.URLInput(attrs={'class': 'form-control mb-2'}),
            'category': forms.Select(attrs={'class': 'form-control mb-2'}),
            'creator': forms.Select(attrs={'class': 'form-control mb-2'}),
            'active': forms.CheckboxInput(attrs={'class': 'largerCheckbox mb-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-2', 'maxlength': '600'}),
            'winner': forms.Select(attrs={'class': 'form-control mb-2'}),
            'creator': forms.TextInput(attrs={'class': 'form-control mb-2', 'id':'creator', 'type':'hidden', 'value': ''}),
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