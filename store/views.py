from django.shortcuts import render


def product_list(request):
    return render(request, "store/product_list.html")


def product_detail(request, pk):
    return render(request, "store/product_detail.html")
