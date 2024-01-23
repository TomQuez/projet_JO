from django.db import models
from django.urls import reverse

from shop.settings import AUTH_USER_MODEL

# Create your models here.
class Offer(models.Model):
    
    """Modèle représentant une offre de billet pour les J.O. de Paris 2024. les administrateurs peuvent créer, modifier et supprimer des offres."""
    
    name=models.CharField(max_length=128)
    slug=models.SlugField(max_length=128)
    price=models.FloatField(default=0.0)
    stock=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    sales_number=models.IntegerField(default=0)
    thumbnail=models.ImageField(upload_to="offer_images",blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} ({self.stock})'
    
    def get_absolute_url(self):
        return reverse('offers')
    
    class Meta:
        ordering=['name']
    
class Blog_article(models.Model):
    
    """Modèle représentant un article de blog, destiné à être affiché sur la page d'accueil, pour présenter les J.O. de Paris 2024. Les administrateurs peuvent créer, modifier et supprimer des articles de blog."""
    
    title=models.CharField(max_length=200)
    description=models.TextField()
    thumbnail=models.ImageField(upload_to="blog_article_images",blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('index')
    
    
class Order(models.Model):
    
    """Modèle destiné à représenter une commande. Les utilisateurs peuvent créer des commandes et les supprimer. La commande est créée lorsqu'un utilisateur ajoute une offre à son panier."""
    
    user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    offer=models.ForeignKey(Offer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    ordered=models.BooleanField(default=False)
    ordered_date=models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return f'{self.offer.name} ({self.quantity})'
    
class Cart(models.Model):
    
    """Modèle destiné à représenter le panier d'un utilisateur. Les utilisateurs peuvent créer, et supprimer leur panier."""
    
    user=models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    orders=models.ManyToManyField(Order)
    
    def __str__(self):
        return f'{self.user.username} cart'
    
    def delete(self,*args,**kwargs):
        self.orders.clear()
        super().delete(*args,**kwargs)
        

class Ticket(models.Model):
    
    """Modèle destiné à représenter un billet. Le billet physique qui sera controlé lors de l'évènement réel est un qr code.Un billet équivaut à un qr code. chaque qr code est généré grâce à une clé unique."""
    
    user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    ticket_key=models.TextField(max_length=1000, blank=True,null=True)
    qrcode_ticket=models.ImageField(upload_to="qrcode",blank=True,null=True)
    ticket_name=models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.user.username} ticket'