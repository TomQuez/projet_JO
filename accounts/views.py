from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout

User=get_user_model()
# Create your views here.
def signup(request):
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        email=request.POST.get('email')
        user=User.objects.create_user(username=name,password=password,first_name=firstname,email=email)  
        login(request,user)
        return redirect('index')
    
    
    return render(request,'accounts/signup.html')

def logout_user(request):
    logout(request)
    return redirect('index')