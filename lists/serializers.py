from rest_framework import serializers
from .models import WishListItem


class WishlistSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=19, decimal_places=2)
    link = serializers.CharField(max_length=500)
    note = serializers.CharField(max_length=500)
    #user_id = serializers.IntegerField()

    def create(self, validated_data):
        return WishListItem.objects.create(**validated_data)

