from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
from store.models import Ticket 
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**kwargs):
        if not email:
            raise ValueError("l'email est obligatoire")
        email=self.normalize_email(email)
        user=self.model(email=email,**kwargs)
        user.set_password(password) 
        user.save()
        return user
    
    def create_superuser(self,email,password,**kwargs):
        kwargs["is_staff"]=True
        kwargs["is_superuser"]=True
        kwargs["is_active"]=True
        return self.create_user(email=email,password=password,**kwargs)


class Shopper(AbstractUser):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username=models.CharField(max_length=254,unique=False)
    email=models.EmailField(unique=True, max_length=254)
    tickets=models.ManyToManyField(Ticket,blank=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()

    def __str__(self):
        return f'{self.last_name} {self.email}'
    
    
   