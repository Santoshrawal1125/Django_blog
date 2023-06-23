from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('aboutus', about, name='aboutus'),
    path('contactus', contact, name='contactus'),
    path('my_portfolio', portfolio, name='my_portfolio'),
    path('price', price, name='price'),
    path('services', services, name='services'),
    path('blog_home', blog_home, name='blog_home'),
    path('blog_single/<int:id>', blog_single, name='blog_single')
]
