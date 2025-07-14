from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):  # Display all products
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})


def product_detail(request, pk):  # Show single product
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})
