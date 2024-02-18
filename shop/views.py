from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from shop.models import Product
from .forms import OrderForm
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

def details(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'shop/details.html', {'product':product})


def checkout(request):
    orderform = OrderForm()
    if request.method == 'POST':
        orderform = OrderForm(request.POST , initial={'total': request.POST.get("total"), 'items': request.POST.get("items")})
        if orderform.is_valid():
            orderform.save()
        return redirect( 'shop:index')
    return render(request, 'shop/checkout.html', {'form': orderform})