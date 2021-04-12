from django.urls import path
from . import views


app_name = 'lists'

urlpatterns = [
    path('wishlist/', views.WishlistListView.as_view(), name='wishlist_list'),
    path('wishlist/<pk>/', views.WishlistDetailView.as_view(), name='wishlist_detail'),
]
