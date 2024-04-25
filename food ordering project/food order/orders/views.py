from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import Item, Order, OrderItem
from .forms import ItemForm


@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'orders/home.html', {'items': items})


@login_required
def view_orders(request):
    orders = {}
    order_items = OrderItem.objects.filter(order__user=request.user).select_related('order', 'item')
    
    for order_item in order_items:
        order_id = order_item.order_id
        if order_id not in orders:
            orders[order_id] = {
                'timestamp': order_item.order.timestamp,
                'items': []
            }
        orders[order_id]['items'].append({
            'name': order_item.item.name,
            'quantity': order_item.quantity
        })
    
    return render(request, 'orders/view_orders.html', {'orders': orders})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required
def place_order(request):
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        for item in Item.objects.all():
            quantity_key = f'quantity_{item.id}'
            quantity = request.POST.get(quantity_key)
            if quantity is not None and int(quantity) > 0:
                OrderItem.objects.create(order=order, item=item, quantity=int(quantity))
        return redirect('view_orders')
    else:
        items = Item.objects.all()
        return render(request, 'orders/home.html', {'items': items})
