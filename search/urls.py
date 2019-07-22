from django.conf.urls import url
from django.contrib import admin
from .views import (searchproducts)

app_name = 'search'

urlpatterns = [
     url(r'^$', searchproducts, name='searchproducts'),
]
