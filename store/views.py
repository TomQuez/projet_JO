from django.shortcuts import render
from .models import Offer,Blog_article
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