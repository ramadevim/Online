from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order,OrderItem
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
               OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()

        return render(request, 'order/created.html', {'order': order})

    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'form': form})