from django.urls import re_path, path
from . import views

app_name = 'shop'

urlpatterns = [
	re_path(r'^$',views.home,name='home'),
	path('about/',views.about,name='about'),
	path('contact/',views.contact,name='contact'),
	path('products/',views.product_list,name='product_list'),
	re_path(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_category'),
	re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
]