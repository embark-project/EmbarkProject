from django.contrib import admin
from django.urls import path, include
from app import views
from .views import index, login, admin_register, mod_register, user_register

admin.autodiscover()

urlpatterns = [
    path('', views.index,name="index"),
    path('admin_register/', views.admin_register, name="admin_register"),
    path('mod_register/', views.mod_register, name="mod_register"),
    path('user_register/', views.user_register, name="user_register"),
    path('login/',views.login,name="login"),
]


