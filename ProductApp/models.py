from django.db import models

# Create your models here.from django.db import models

class Category(models.Model):
    """ Model to Category """
    name = models.CharField(max_length=50, null=False)
    description=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'name:{self.name}'
    
class Product(models.Model):
    """ Model to Products """
    name = models.CharField(max_length=50, null=False)
    description=models.TextField(blank=True)
    price=models.PositiveIntegerField(null=False )
    stock=models.SmallIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category=models.ManyToManyField(Category,through='ProductCategory')

    def __str__(self):
        return f'name:{self.name}-proce:{self.price}-stock:{self.stock}'
    


class Order(models.Model):
    """ Model to order """
    shippingAdress = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    product=models.ManyToManyField(Product,through='ProductOrder')

    def __str__(self):
        return f'OrderId:{self.id}-CreateDate:{self.created_at}'

class ProductCategory(models.Model):
    """Table to create relationship with many to many on Product and Category"""
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)

class ProductOrder(models.Model):
    """Table to create relationship with many to many on Product and Order"""
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)