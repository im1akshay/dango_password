from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('passw/', views.passw, name = 'pass'),
    path('about/', views.about, name = 'about'),
]
