from django.urls import path
from . import views

app_name = "leafpost"
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('login/', views.login_view, name='login_view'), 
    path('signup/', views.signup_view, name='signup_view'),  
    # path('create/', views.create_post, name='create_post'),
    # path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('logout/', views.logout_view, name='logout'),
]
