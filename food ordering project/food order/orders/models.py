from django.db import models
from django.contrib.auth.models import User, Group, Permission

class Item(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        permissions = [
            ('can_add_item', 'Can add item'),
            ('can_change_item', 'Can change item'),
            ('can_delete_item', 'Can delete item'),
        ]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
