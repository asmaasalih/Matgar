from django.shortcuts import render, get_object_or_404, redirect
from .models import Category,Product
from cart.forms import CartAddProductForm
from .forms import ContactForm
# Create your views here.

def home(request,category_slug=None):
	category = None
	categories = Category.objects.all()
	if category_slug:
		category = get_object_or_404(Category,slug=category_slug)

	context = {
		'category':category,
		'categories':categories
	}
	return render(request,'shop/product/home.html',context)	


def product_list(request,category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category,slug=category_slug)
		products = products.filter(category=category)

	else:
		products = Product.objects.filter(available=True)

	context = {
		'category':category,
		'categories':categories,
		'products':products
	}
	return render(request,'shop/product/products.html',context)

def product_detail(request,id,slug):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	product = get_object_or_404(Product,id=id,slug=slug,available=True)
	cart_product_form = CartAddProductForm()
	context = {
		'category':category,
		'categories':categories,
		'products':products,
		'product':product,
		'cart_product_form':cart_product_form,
	}
	return render(request,'shop/product/detail.html',context)


def contact(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			#email = form.changed_data['email']
			content = form.cleaned_data['content']
			return redirect('shop:home')

	else:
		form = ContactForm()
	
	context = {
		'title':'تواصل معنا',
		'content':'مرحبا بك في صفحة التواصل',
		'form':form,
	}
	return render(request,'contact/contact.html',context)


def about(request):
	template_name = 'about/about.html'
	context = {
		'title':'عن الشركة'
	}
	return render(request,template_name,context)
