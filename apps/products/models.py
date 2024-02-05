from django.db import models

# Create your models here.





class Category(models.Model):
    
    category_name = models.CharField('Name of category', max_length=255, blank=False , null=False, unique=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.category_name
    
# Product  
class Product(models.Model):
    """Model definition for Product."""
    ELABORATION_CHOICES = [
        ('Kitchen', 'Kitchen'),
        ('Bar', 'Bar'),
        ('Waiter', 'Waiter'),
    ]
    elaboration = models.CharField('Order paid',max_length=13,default='Kitchen' ,choices=ELABORATION_CHOICES, blank=False, null=False)
    product_name = models.CharField('Name of product', max_length=255, blank=False , null=False)
    cost = models.DecimalField('Cost', max_digits=10,  decimal_places=2, blank= False, null= False)
    active = models.BooleanField(default=True)
    discount = models.PositiveIntegerField('Discount of product in %', default=0, blank=False, null=False)
    image = models.ImageField('Image of product', upload_to='product_image/', blank=True, null=True)
    category = models.ForeignKey(Category,related_name='productCategory', on_delete=models.CASCADE, verbose_name='Category',blank=False, null= False)
    # Define fields here

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'id: {self.id}. {self.product_name}'
    
    
    

class Aggregate(models.Model):
    """Model definition for Aggregate."""
    agregate_name = models.CharField('Name of aggregate', max_length=255, blank=False , null=False)
    measurement_unit = models.CharField('Unit of measurement', max_length=50, blank=False , null=False)
    measurement_unit_quantity = models.DecimalField('Quantity unit of measurement', max_digits=10,  decimal_places=2, blank= False, null= False)
    cost = models.DecimalField('Cost', max_digits=10,  decimal_places=2, blank= False, null= False)
    product = models.ForeignKey(Product,related_name='agregateProduct', on_delete=models.CASCADE, verbose_name='Product',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Aggregate."""

        verbose_name = 'Aggregate'
        verbose_name_plural = 'Aggregates'

    def __str__(self):
        return f'id:{self.id} {self.agregate_name}. id:{self.product.id} Product {self.product.product_name}'


class Ingredient(models.Model):
    """Model definition for Ingredient."""
    ingredient_name = models.CharField('Name of ingredient', max_length=255, blank=False , null=False)
    product = models.ForeignKey(Product,related_name='ingredientProduct', on_delete=models.CASCADE, verbose_name='Ingredient',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Ingredient."""

        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.ingredient_name
