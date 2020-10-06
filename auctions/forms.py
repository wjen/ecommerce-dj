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

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('title', 'comment')
    #     widgets = {
    #         'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
    #         'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment'})
    #     }

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].label = ''
    #     self.fields['comment'].label = ''