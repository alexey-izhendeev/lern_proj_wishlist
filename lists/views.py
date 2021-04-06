from django.shortcuts import render
from .models import WishListItem
from .forms import WishForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import WishlistSerializer


def index(request):  # main page
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'lists/index.html', {
        'lists': WishListItem.objects.all(),
    })


def user_wishes(request, user_id):  # all items of wishlist
    wishlist = WishListItem.objects.all().filter(userid=user_id)
    user = User.objects.get(pk=user_id)
    return render(request, 'lists/user.html', {
        'wishlist': wishlist,
        'user': user
    })


def add_item(request, user_id):  # adds an item to wishlist
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.userid = request.user
            item.save()
            return HttpResponseRedirect(reverse('user', args=[user_id]))
    else:
        form = WishForm()
    return render(request, 'lists/wishlist_edit.html', {
            'form': form
        })


def delete_item(request, user_id):  # delits an item from wishlist
    if request.method == 'POST':
        item = WishListItem.objects.get(pk=int(request.POST['item']))
        item.delete()
        return HttpResponseRedirect(reverse('user', args=[user_id]))


def edit_item(request, user_id):  # redirects to a page, where item can be edited
    if request.method == 'POST':
        item = WishListItem.objects.get(pk=int(request.POST['item']))

        return render(request, 'lists/edit_item.html', {
            'item': item,
        })


def save_item(request, user_id, item_id):  # when item is edited(updated) it saves the item
    if request.method == 'POST':
        item = WishListItem.objects.get(pk=item_id)
        item.name = request.POST['name']
        item.price = request.POST['price']
        item.link = request.POST['link']
        item.note = request.POST['note']
        item.save()

        return HttpResponseRedirect(reverse('user', args=[user_id]))


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


class WishlistView(APIView):
    def get(self, request):
        wishlist = WishListItem.objects.all()
        serializer = WishlistSerializer(wishlist, many=True)
        return Response({'wishlist': serializer.data})

    def post(self, request):
        item = request.data.get('item')
        serializer = WishlistSerializer(data=item)
        if serializer.is_valid(raise_exception=True):
            item_saved = serializer.save()
        return Response({'success': f'Item {item_saved} created successfully'})





