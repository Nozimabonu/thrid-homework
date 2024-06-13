from django.shortcuts import render, get_object_or_404

from app.models import Product


# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'app/index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    # product = get_object_or_404(Product, pk=pk)
    attributes = product.get_attributes()
    context = {
        'product': product,
        'attributes': attributes
    }
    return render(request, 'app/product-detail.html', context)
