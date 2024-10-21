from django.urls import path
from . import views

urlpatterns = [
    path('LeafPost/', views.home_page, name='home_page'),
    path('LeafPost/login/', views.login_page, name='login_page'), 
    path('LeafPost/signup/', views.signup_page, name='signup_page'),  
]
