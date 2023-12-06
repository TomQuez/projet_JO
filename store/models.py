from django.db import models
from django.urls import reverse

# Create your models here.
class Offer(models.Model):
    name=models.CharField(max_length=128)
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
    title=models.CharField(max_length=200)
    description=models.TextField()
    thumbnail=models.ImageField(upload_to="blog_article_images",blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('index')