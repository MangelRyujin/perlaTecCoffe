from django.db import models
from apps.products.models import Aggregate, Product
from apps.users.models import User
from apps.restaurant.models import Table

# Create your models here.

class TimeTransfer(models.Model):
    
    date = models.DateField('Fecha', auto_now_add=True, null=True)
    time = models.TimeField('Hora', auto_now_add=True, null=True)
    
    """docstring for ClassName."""
    class Meta:
        abstract = True
    
# Order  
class Order(TimeTransfer):
    STATE_CHOICES = [
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid')
    ]
    PAID_CHOICES = [
        ('Transfer', 'Transfer'),
        ('Cash', 'Cash'),
        ('Both', 'Both'),
        
    ]
    amount = models.DecimalField('Amount', max_digits=10,  decimal_places=2, blank= False, null= False)
    state = models.CharField('Order state',max_length=13,default='Unpaid' ,choices=STATE_CHOICES, blank=False, null=False)
    paid = models.CharField('Order paid',max_length=13,default='Cash' ,choices=PAID_CHOICES, blank=False, null=False)
    transfer = models.DecimalField('Transfer', max_digits=10,  decimal_places=2, blank= True, null= True)
    cash = models.DecimalField('Cash', max_digits=10,  decimal_places=2, blank= True, null= True)
    user = models.ForeignKey(User,related_name='orderUser', on_delete=models.CASCADE, verbose_name='User',blank=False, null= False)
    table = models.ForeignKey(Table,related_name='orderTable', on_delete=models.CASCADE, verbose_name='Table',blank=False, null= False)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        """Unicode representation of Order."""
        return f'{self.amount} in table {self.table.number}'
    
    def paidOrder(self):
        self.state = 'Paid'
        self.save
    
# itemsOrder  
class Items(models.Model):
    """Model definition for Items."""
    cant = models.PositiveIntegerField('Quantity of product', default=1, blank=False , null=False)
    amount = models.DecimalField('Amount', max_digits=10,  decimal_places=2, blank= False, null= False)
    order = models.ForeignKey(Order,related_name='itemsOrder', on_delete=models.CASCADE, verbose_name='Order',blank=False, null= False)
    product = models.ForeignKey(Product,related_name='itemsProduct', on_delete=models.CASCADE, verbose_name='Product',blank=False, null= False)
    # Define fields here

    class Meta:
        """Meta definition for Items."""

        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.cant}x  {self.product} . Price {self.amount}'
    

class AggregateItems(models.Model):
    """Model definition for AggregateItems."""
    aggregate = models.ForeignKey(Aggregate,related_name='aggregateitemAgregate', on_delete=models.CASCADE, verbose_name='Aggregate',blank=False, null= False)
    item = models.ForeignKey(Items,related_name='aggregateitemItems', on_delete=models.CASCADE, verbose_name='Item',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Aggregate."""

        verbose_name = 'Aggregate Item'
        verbose_name_plural = 'Aggregates Items'

    def __str__(self):
        return f'id: {self.id}. {self.aggregate.agregate_name}'