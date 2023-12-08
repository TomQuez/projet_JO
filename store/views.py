from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import Offer,Blog_article,Cart,Order
from django.http import JsonResponse
from django.db import transaction
import uuid
import qrcode
# Create your views here.




def index(request):
    return render(request,'store/index.html')

def get_blog_articles(request):
    blog_articles=Blog_article.objects.all()
    data=[]
    for article in blog_articles:
        object={
            'title':article.title,
            'description':article.description,
            'thumbnail':article.thumbnail.url
        }
        data.append(object)
    context={
        'data':data,
    }
    return JsonResponse(context)

def offers(request):
    offers=Offer.objects.all()
    context={
        'offers':offers,
    }
    return render(request,'store/offers.html',context)

def get_offers_data(request):
    offers=Offer.objects.all()
    data=[]
    for offer in offers:
        object={
            'name':offer.name,
            'price':offer.price,
            'slug':offer.slug,
            'stock':offer.stock,
            'description':offer.description,
            'sales_number':offer.sales_number,
            'thumbnail':offer.thumbnail.url
        }
        data.append(object)
    context={
        'data':data,
    }
    return JsonResponse(context)

def offer_detail(request,slug):
    offer=get_object_or_404(Offer,slug=slug)
    context={
        'offer':offer,
    }
    return render(request,'store/offer_detail.html',context)


def add_to_cart(request,slug):
    user=request.user
    offer=get_object_or_404(Offer,slug=slug)
    cart, _ =Cart.objects.get_or_create(user=user)
    order,created=Order.objects.get_or_create(user=user,ordered=False,offer=offer)
    
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity+=1
        order.save()
        
    return redirect(reverse("offer-detail",kwargs={"slug":slug}))
    
    
def cart(request):
    
    cart=get_object_or_404(Cart,user=request.user)
    total_price=0
    total_quantity=0
    for order in cart.orders.all():
        total_price+=order.offer.price*order.quantity
        
    for order in cart.orders.all():
        total_quantity+=order.quantity    
    
    
    context={
        'orders':cart.orders.all(),
        'total_price':total_price,
        'total_quantity':total_quantity,
    }
    
    
    
    return render(request,'store/cart.html',context=context)

# def create_checkout_session(request):
#     if cart:=request.user.cart:
#         cart.ordered()
      
    
#     return redirect('index')
@transaction.atomic
def checkout(request):
    cart=get_object_or_404(Cart,user=request.user)
    unique_keys=[]
    unique_qrcode=[]
    
    for order in cart.orders.all():
        unique_key=str(uuid.uuid4())+str(request.user.id)+str(order.id)
        unique_keys.append(unique_key)
        order.ordered=True
        order.offer.stock-=order.quantity
        order.offer.sales_number+=order.quantity
        order.save()
        order.offer.save()
        qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=5)
        qr.add_data(unique_key)
        qr.make(fit=True)
        img=qr.make_image(fill='black',back_color='white')
        qrcode_path=f'media/qrcode/{unique_key}.png'
        img.save(qrcode_path)
        
        
        
    cart.delete()
    
    
    return render(request,'store/checkout.html',context={})

def delete_cart(request):
    if cart := request.user.cart:
        
        cart.delete()   
    
    
    return redirect('index')