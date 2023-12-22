from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import Offer,Blog_article,Cart,Order,Ticket
import datetime
from django.http import JsonResponse
from django.db import transaction
import uuid
import qrcode
from botocore.exceptions import NoCredentialsError
import boto3
import os
from io import BytesIO

from decouple import config
from shop.settings import BASE_DIR, AWS_LOCATION,AWS_S3_CUSTOM_DOMAIN
# Create your views here.




def index(request):
    
    """Vue de la page d'accueil, qui affiche les articles de blog."""
    
    return render(request,'store/index.html')

def get_blog_articles(request):
    
    """Vue qui renvoie les articles de blog au format JSON, afin qu'il soit récupéré par le code javascript de façon dynamique."""
    
    blog_articles=Blog_article.objects.all()
    data=[]
    for article in blog_articles:
        object={
            'title':article.title,
            'description':article.description,
            'thumbnail':f'https://django-media-4327.s3.eu-north-1.amazonaws.com/media/{article.thumbnail.name}',
        }
        data.append(object)
    context={
        'data':data,
    }
    return JsonResponse(context)

def offers(request):
    
    """Vue qui affiche les offres de billets vendues sur le site."""
    
    offers=Offer.objects.all()
    context={
        'offers':offers,
    }
    return render(request,'store/offers.html',context)

def get_offers_data(request):
    
    """Vue qui renvoie les offres de billets au format JSON, afin qu'il soit récupéré par le code javascript de façon dynamique."""
    
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
            'thumbnail':f'https://django-media-4327.s3.eu-north-1.amazonaws.com/media/{offer.thumbnail.name}',
            'thumbnail_url':offer.thumbnail.url,
            'thumbnail_name':offer.thumbnail.name,
        }
        data.append(object)
    context={
        'data':data,
    }
    return JsonResponse(context)

def offer_detail(request,slug):
    
    """Vue qui affiche les détails d'une offre de billet. c'est sur cette page que l'utilisateur peut cliquer sur le lien pour ajouter l'offre à son panier."""
    
    offer=get_object_or_404(Offer,slug=slug)
    context={
        'offer':offer,
    }
    return render(request,'store/offer_detail.html',context)


def add_to_cart(request,slug):
    
    """Vue qui ajoute une offre de billet au panier de l'utilisateur."""
    
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
    
    """Vue qui affiche le panier de l'utilisateur."""
    
    
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


@transaction.atomic
def checkout(request):
    
    """Vue qui permet à l'utilisateur de passer commande. Lorsque l'utilisateur passe commande, un ticket est créé pour chaque billet acheté, et un QR code est généré pour chaque ticket."""
    
    cart=get_object_or_404(Cart,user=request.user)
    unique_keys=[]
    
    s3=boto3.client('s3',aws_access_key_id=config('AWS_ACCESS_KEY_ID'),aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),region_name='eu-north-1')
    
    
    for order in cart.orders.all():
        
        
        
        order.ordered=True
        order.offer.stock-=order.quantity
        order.offer.sales_number+=order.quantity
        order.ordered_date=datetime.datetime.now()  
        
        order.save()
        order.offer.save()
        
        for i in range(order.quantity):
            unique_key=str(uuid.uuid4())+str(request.user.id)
            date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            unique_keys.append(unique_key)
            ticket=Ticket.objects.create(user=request.user)
            qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=5)
            qr.add_data(unique_key)
            qr.make(fit=True)
            img=qr.make_image(fill='black',back_color='white')
            ticket.ticket_name=f'{order.offer.slug}_{i+1}_{date}'[:50]
            qrcode_path=f'media/qrcode/{ticket.ticket_name}.png'
            s3_key=f'qrcode/{ticket.ticket_name}.png'
            img.save(qrcode_path)
            
            
            ticket.qrcode_ticket=qrcode_path
            ticket.save()   

            try : 
                s3.upload_file(
                    Filename=qrcode_path,
                    Bucket=config('AWS_STORAGE_BUCKET_NAME'),
                    Key=s3_key,
                    ExtraArgs={'ACL':'public-read'}
                )
            except Exception as e:
                print(f'error uploading file : {e}' )    

        
            request.user.tickets.add(ticket) 
        
        
        
    cart.delete()
    
    
    return render(request,'store/checkout.html',context={})

def delete_cart(request):
    
    """Vue qui supprime le panier de l'utilisateur."""
    
    if cart := request.user.cart:
        
        cart.delete()   
    
    
    return redirect('index')

def orders_paid(request):
    
    """Vue qui affiche les billets achetés par l'utilisateur."""
    
    tickets=request.user.tickets.all()
    context={
        'tickets':tickets,
    }
    return render(request,'store/orders_paid.html',context=context)