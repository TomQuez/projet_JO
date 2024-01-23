from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate
import time
from store.models import Cart


User=get_user_model()

def signup(request):
    
    """Vue qui permet à un utilisateur de s'inscrire."""
    
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('username')
        email=request.POST.get('email')
        user=User.objects.create_user(username=name,password=password,last_name=lastname,first_name=firstname,email=email)  
        # si le visiteur qui vient de s'inscrire possedait un cart, on le récupère
        if 'visitor_cart_id' in request.session:
            cart_id=request.session['visitor_cart_id']
            cart=Cart.objects.get(id=cart_id)
            cart.user=user
            cart.save()
            del request.session['visitor_id']
            del request.session['visitor_has_selected_offer']
            del request.session['visitor_cart_quantity']
            
        login(request,user)
        return redirect('index')
    
    
    return render(request,'accounts/signup.html')

def login_user(request):
    
    """Vue qui permet à un utilisateur de se connecter."""
    
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        time.sleep(3)
        user=authenticate(username=name,password=password)
        if user:
            if 'visitor_cart_id' in request.session:
                cart_id=request.session['visitor_cart_id']
                cart=Cart.objects.get(id=cart_id)
                cart.user=user
                cart.save()
                del request.session['visitor_id']
                del request.session['visitor_has_selected_offer']
                del request.session['visitor_cart_quantity']
            login(request,user)
            return redirect('index')
        else:
            return render(request,'accounts/login.html',{'message':'Les informations de connexion sont incorrectes'})
        
    return render(request,'accounts/login.html')



def logout_user(request):
    
    
    """Vue qui permet à un utilisateur de se déconnecter."""
    
    
    logout(request)
    request.session.flush()
    
    return redirect('index')
