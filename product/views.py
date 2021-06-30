from django.shortcuts import render
from . models import *

# Create your views here.

def products(request):
    allproducts=ProductList.objects.all
    context= {'allproducts': allproducts}
    return render(request, 'product.html', context)
