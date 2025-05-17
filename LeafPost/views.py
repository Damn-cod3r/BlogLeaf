from django.shortcuts import render, redirect
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from django import forms
# from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
# Define the PostForm here inside views.py
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'image', 'categories', 'is_featured']

# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             # Save M2M fields after saving the post object
#             form.save_m2m()
#             return redirect(post.get_absolute_url())  # redirect to the new post detail page
#     else:
#         form = PostForm()
#     return render(request, 'LeafPost/create_post.html', {'form': form})

def home_view(request):
    return render(request, 'LeafPost/home.html')

# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'LeafPost/post_detail.html', {'post': post})

# Define the Signup form here



def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash password
            user.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('leafpost:login_view')
    else:
        form = SignupForm()
    return render(request, 'LeafPost/signup.html', {'form': form})

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data

# Define the Login form here
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('leafpost:home_view')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'LeafPost/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('leafpost:home_view')