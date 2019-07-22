from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200,db_index=True,unique=True)
	img  = models.ImageField(upload_to='media',blank=True)

	class Meta: 
		ordering = ('name',)
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __str__(self):                           
		return self.name        
		
	def get_absolute_url(self):
		return reverse('shop:product_list_category',args=[self.slug])	

	

class Product(models.Model):
	caliber_choices = (
		('18','18'),
		('21','21'),
	)

	category  = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
	name 	  = models.CharField(max_length=200,db_index=True)
	slug 	  = models.SlugField(max_length=200,db_index=True)
	image 	  = models.ImageField()
	weight    = models.FloatField(default=True)
	caliber   = models.CharField(max_length=2,choices=caliber_choices,default='21')
	price 	  = models.DecimalField(max_digits=10,decimal_places=2)
	stock 	  = models.PositiveIntegerField()
	tax       = models.FloatField(default=True)
	available = models.BooleanField(default=True)
	created   = models.DateTimeField(auto_now_add=True)
	updated	  = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ('-created',)
		index_together = (('id','slug'))
		verbose_name = "Product"
		verbose_name_plural = "Products"

	def __str__(self):
		return self.name	

	def get_absolute_url(self):
		return reverse('shop:product_detail',args=[self.id,self.slug])