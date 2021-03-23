from django import forms
from .models import WishListItem


class WishForm(forms.ModelForm):

    class Meta:
        model = WishListItem
        fields = ('name', 'price', 'link', 'note')

'''class User(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first} {self.last}'''