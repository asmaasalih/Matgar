from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.models import Product



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=1,choices=(('M','Male'),('F','Female')),blank=True)
    age = models.PositiveIntegerField(null=True,blank=True)
    products = models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'profile' 
        verbose_name_plural = 'profiles'       


