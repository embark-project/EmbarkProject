from django.contrib import admin
from django.urls import path, include
from app import views
from .views import index, register,login

admin.autodiscover()

urlpatterns = [
    path('', views.index,name="index"),
    path('register/', views.register, name="register"),
    path('login/',views.login,name="login"),
]


