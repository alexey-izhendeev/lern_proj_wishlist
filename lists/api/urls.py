from django.urls import path
from . import views


app_name = 'lists'

urlpatterns = [
    path('wishlist/', views.WishlistListView.as_view(), name='wishlist_list'),
    path('wishlist/<pk>/', views.WishlistDetailView.as_view(), name='wishlist_detail'),
    path('wishlist/<pk>/view', views.DeleteItem.as_view(), name='view_item'),
]
