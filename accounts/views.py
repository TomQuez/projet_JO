from django.shortcuts import render
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your views here.
def signup(request):
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        email=request.POST.get('email')
    
    
    return render(request,'accounts/signup.html')