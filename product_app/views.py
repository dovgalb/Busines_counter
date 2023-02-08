from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def show_main_page(request):
    c = 2
    print(2+2+c)
    return render(request, 'product_app/main_page.html')


def show_all_products(request):
    products = Product.objects.all()
    for product in products:
        product.save()
    return render(request, 'product_app/all_product.html', context={
        'products': products,
    })


def show_one_product(request, slug_product: str):
    product = get_object_or_404(Product, slug=slug_product)

    return render(request, 'product_app/one_product.html', context={
        'product': product,
    })
