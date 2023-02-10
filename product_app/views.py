from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def show_main_page(request):
    """
    из pull_request
    проверка pull request
    :param request:
    :return:
    """
    return render(request, 'product_app/main_page.html')


def show_all_products(request):
    """
    из pull_request
    :param request:
    :return:
    """
    products = Product.objects.all()
    for product in products:
        product.save()
    return render(request, 'product_app/all_product.html', context={
        'products': products,
    })


def show_one_product(request, slug_product: str):
    """
    из pull_request
    :param request:
    :param slug_product:
    :return:
    """
    product = get_object_or_404(Product, slug=slug_product)

    return render(request, 'product_app/one_product.html', context={
        'product': product,
    })
