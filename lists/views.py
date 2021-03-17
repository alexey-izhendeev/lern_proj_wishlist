from django.shortcuts import render
from .models import WishListItem, User

def index(request):
    return render(request, 'lists/index.html', {
        'lists': WishListItem.objects.all(),
    })

def user_wishes(request, user_id):
    wishlist = WishListItem.objects.all().filter(userid=user_id)
    user = User.objects.get(pk=user_id)
    return render(request, 'lists/user.html', {
        'wishlist': wishlist,
        'user': user
    })
