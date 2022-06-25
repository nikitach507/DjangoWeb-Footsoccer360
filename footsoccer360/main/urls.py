from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('gift_form', views.gift_form, name='gift_form'),
    path('gift_info', views.gift_home, name='gift_info'),
]