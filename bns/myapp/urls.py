from django.conf.urls import url
from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
    path('listing_submission/', views.listing_submission, name='account'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register')
]