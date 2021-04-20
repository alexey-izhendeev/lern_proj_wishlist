from rest_framework import generics
from ..models import WishListItem
from .serializers import WishListSerializer

class WishlistListView(generics.ListAPIView):

    queryset = WishListItem.objects.all()
    serializer_class = WishListSerializer


class WishlistDetailView(generics.RetrieveAPIView):

    queryset = WishListItem.objects.all()
    serializer_class = WishListSerializer
