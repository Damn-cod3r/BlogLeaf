from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from .models import *

def home_view(request):
    return render(request, 'LeafPost/home.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']  
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already Exists")
                return redirect('leafpost:signup_view')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already Exists")
                return redirect('leafpost:signup_view')
            else:
                User.objects.create_user(username=username, email=email, password=password).save()
                return redirect('leafpost:login_view')
        else:
            messages.info(request, "Password should match")
            return redirect('leafpost:signup_view')
            
    return render(request, "LeafPost/signup.html")

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')    
        email = request.POST.get('email')  
        message = request.POST.get('message')  
        obj = Contact(name=name, email=email, message=message)
        obj.save()
        messages.success(request, f"Dear {name}, Thanks for your time!")
        return redirect('leafpost:contact_view')  
    return render(request, "LeafPost/contact.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("leafpost:home_view")
        else:
            messages.info(request,'Username or Password is incorrect')
            return redirect("leafpost:login_view")
            
    return render(request,"LeafPost/login.html")

def logout_view(request):
    logout(request)
    return redirect('leafpost:home_view')


