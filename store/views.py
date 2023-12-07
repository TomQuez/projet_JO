from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import Offer,Blog_article,Cart,Order
from django.http import JsonResponse
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
    order,created=Order.objects.get_or_create(user=user,offer=offer)
    
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity+=1
        order.save()
        
    return redirect(reverse("offer-detail",kwargs={"slug":slug}))
    
    
def cart(request):
    pass