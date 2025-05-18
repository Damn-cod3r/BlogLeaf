from django.urls import path
from . import views

app_name = "leafpost"
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('login/', views.login_view, name='login_view'), 
    path('signup/', views.signup_view, name='signup_view'),  
    path('contact/', views.contact_view, name='contact_view'),
    path('create/', views.create_post_view, name='create_post_view'),
    path('profile/', views.profile_view, name='profile_view'),
    # path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('logout/', views.logout_view, name='logout_view'),
]
