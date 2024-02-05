from django.db import models
from apps.products.models import Aggregate, Product
from apps.users.models import User
from apps.restaurant.models import Table
from apps.orders.models import Items, Order

# Create your models here.

class TimeTransfer(models.Model):
    
    date = models.DateField('Fecha', auto_now_add=True, null=True)
    time = models.TimeField('Hora', auto_now_add=True, null=True)
    
    """docstring for ClassName."""
    class Meta:
        abstract = True
    
# Notification  
class Notification(TimeTransfer):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, verbose_name='Items',blank=False, null= False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User',blank=False, null= False)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Notification."""

        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        """Unicode representation of Notification."""
        return f'{self.item.product.product_name} in table {self.item.order.table.number}'