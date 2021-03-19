from django.shortcuts import render
from .models import WishListItem
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
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


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'lists/login.html', {
                'message': 'Invalid login or pass.'
            })
    return render(request, 'lists/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'lists/login.html', {
        'message': 'Logged out.'
    })
