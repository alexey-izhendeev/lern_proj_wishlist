from django import forms
from .models import WishListItem


class WishForm(forms.ModelForm):

    class Meta:
        model = WishListItem
        fields = ('name', 'price', 'link', 'note', 'userid')
