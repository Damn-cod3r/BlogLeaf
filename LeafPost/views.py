from django.shortcuts import render

def home_page(request):
    return render(request, 'LeafPost/home.html')

def login_page(request):
    return render(request, 'LeafPost/login.html')

def signup_page(request):
    return render(request, 'LeafPost/signup.html')