from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
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

@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        bio = request.POST.get('bio', '')
        location = request.POST.get('location', '')
        birth_date = request.POST.get('birth_date', '')
        profile_picture = request.FILES.get('profile_picture')

        profile.bio = bio
        profile.location = location
        profile.birth_date = birth_date if birth_date else None
        if profile_picture:
            profile.profile_picture = profile_picture

        profile.save()
        return redirect('leafpost:profile_view')

    context = {
        'profile': profile
    }
    return render(request, 'leafpost/profile.html', context)

@login_required
def create_post_view(request):
    class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ['title', 'content', 'image', 'categories', 'is_featured']
            widgets = {
                'title': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Your post title...'
                }),
                'content': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your story here...',
                    'rows': 7
                }),
                'image': forms.ClearableFileInput(attrs={
                    'class': 'form-control'
                }),
                'categories': forms.Select(attrs={
                    'class': 'form-select'
                }),
                'is_featured': forms.CheckboxInput(attrs={
                    'class': 'form-check-input'
                }),
            }

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('leafpost:home_view')
    else:
        form = PostForm()

    return render(request, 'LeafPost/create-post.html', {'form': form})
