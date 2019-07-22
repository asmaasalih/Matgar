from django.shortcuts import render
from django.views.generic import ListView
from shop.models import Product, Category
from django.db.models import Q


def searchproducts(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(name__icontains=query) | Q(caliber__icontains=query)

            results= Product.objects.filter(lookups).distinct()

            context={
                'results': results,
                'submitbutton': submitbutton,
		        'categories':categories,
		        'products':products,
                    }

            return render(request, 'search/search.html', context)

        else:
            return render(request, 'search/search.html')

    else:
        return render(request, 'search/search.html')


