from django.db import models
from django.contrib.auth.models import User


class WishListItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    link = models.CharField(max_length=500)
    note = models.CharField(max_length=500)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.name





