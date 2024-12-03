from django.shortcuts import render

# Create your views here.
def indexview(request):
    return render (request,'index.html')

def list_products(request):
    """
    returns product list page
    """
    return render (request,'products.html')

def detail_product(request):
    return render (request,'productdetail.html')

