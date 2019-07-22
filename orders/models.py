from django.db import models
from shop.models import Product
from decimal import Decimal

# Create your models here.
class order(models.Model): 
    Pay_Choices =(
        ('1','Cash On Delivery'),
        ('2','PayPal'), 
    )
    first_name 	= models.CharField(max_length=50)
    last_name	= models.CharField(max_length=50)
    email 		= models.EmailField()
    address 	= models.CharField(max_length=250)
    city 		= models.CharField(max_length=100)
    region      = models.CharField(max_length=100,default='makah')
    created 	= models.DateTimeField(auto_now_add=True)
    updated 	= models.DateTimeField(auto_now=True)
    paid 		= models.BooleanField(default=False)
    pay_method  = models.CharField(max_length=100, choices=Pay_Choices,null=True,default='Cash On ..')


    class Meta:
        ordering = ('-created',)
        verbose_name = "order"
        verbose_name_plural = "orders"


    def __str__(self):
        return 'Order {}'.format(self.id)   

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order 		= models.ForeignKey(order,related_name='items',on_delete=models.CASCADE)
    product 	= models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price 		= models.DecimalField(max_digits=10,decimal_places=2)
    quantity	= models.PositiveIntegerField(default=1) 

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        return '{}'.format(self.id)    

    def get_cost(self):
        return self.price * self.quantity



