from django.shortcuts import render,get_object_or_404,Http404
from django.views.generic import DetailView,ListView
from .models import Product
from cart.forms import CartAddProductForm



def products_list(request):
    queryset=Product.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,'product/list.html',context)

def product_detail(request, pk,slug):
    product = get_object_or_404(Product,pk=pk, slug=slug)
    cart_add_form =CartAddProductForm()
    return render(request,"product/detail.html",{"product":product,
                                                  "cart_add_form":CartAddProductForm})
