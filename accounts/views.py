from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate

User=get_user_model()
# Create your views here.
def signup(request):
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('username')
        email=request.POST.get('email')
        user=User.objects.create_user(username=name,password=password,last_name=lastname,first_name=firstname,email=email)  
        login(request,user)
        return redirect('index')
    
    
    return render(request,'accounts/signup.html')

def login_user(request):
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=name,password=password)
        if user:
            login(request,user)
            return redirect('index')
        
    return render(request,'accounts/login.html')



def logout_user(request):
    logout(request)
    return redirect('index')