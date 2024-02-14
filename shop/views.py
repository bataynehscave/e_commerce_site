from django.shortcuts import render
from django.core.paginator import Paginator
from shop.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    
    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = products.filter(title__icontains = item_name)

    #pagination code
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'shop/index.html', {"products": products})