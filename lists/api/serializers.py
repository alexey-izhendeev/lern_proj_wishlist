from rest_framework import serializers
from ..models import WishListItem


class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishListItem
        fields = ['id', 'name', 'price', 'link', 'note', 'userid']
