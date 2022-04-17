from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist

def cart_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


# Create your views here.
def cart_details(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(car_id=cart_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prod.price*i.qnty)
            count+=i.qnty
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html',{'ci': ct_items,'tt':tot,'cn':count})


def add_cart(request, product_id):
    prodt = products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(car_id=cart_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(car_id=cart_id(request))
        ct.save()
    try:
        c_item=items.objects.get(prod=prodt,cart=ct)
        if c_item.qnty < c_item.prod.stock:
            c_item.qnty+=1
        c_item.save()
    except items.DoesNotExist:
        c_item=items.objects.create(prod=prodt,qnty=1,cart=ct)
        c_item.save()
    return redirect('cartdetails')


def min_cart(request,product_id):
    ct=cartlist.objects.get(car_id=cart_id(request))
    pro=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prod=pro,cart=ct)
    if c_items.qnty>1:
        c_items.qnty-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')


def delete(request,product_id):
    ct = cartlist.objects.get(car_id=cart_id(request))
    pro = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(prod=pro, cart=ct)
    c_items.delete()
    return redirect('cartdetails')
