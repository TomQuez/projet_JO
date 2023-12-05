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