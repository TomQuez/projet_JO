from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
from store.models import Ticket 
from django.core.validators import RegexValidator
# Create your models here.

class CustomUserManager(BaseUserManager):
    
    """Modèle qui gère la création d'un utilisateur."""
   
    
    def create_user(self,email,password,**kwargs):
        if not email:
            raise ValueError("l'email est obligatoire")
        if not password:
            raise ValueError("le mot de passe est obligatoire")
        if len(password)<8:
            raise ValueError("le mot de passe doit contenir au moins 8 caractères")
        if not any(char.islower() for char in password):
            raise ValueError("le mot de passe doit contenir au moins une minuscule")
        if not any(char.isupper() for char in password):
            raise ValueError("le mot de passe doit contenir au moins une majuscule")
        if not any(char.isdigit() for char in password):
            raise ValueError("le mot de passe doit contenir au moins un chiffre")
        if not any(char in ["@","$","#","%","&","*"] for char in password):
            raise ValueError("le mot de passe doit contenir au moins un caractère spécial")
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
    
    """Modèle qui définit un utilisateur."""
  
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    
    username=models.CharField(max_length=254,unique=False)
    email=models.EmailField(unique=True, max_length=254)
    tickets=models.ManyToManyField(Ticket,blank=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()

    def __str__(self):
        return f'{self.last_name} {self.email}'
    
    
   