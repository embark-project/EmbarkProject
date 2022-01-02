from django.contrib import admin
from django.urls import path, include
from app import views
from .views import index, admin_login, mod_login, user_login 
from .views import admin_register, mod_register, user_register

admin.autodiscover()

urlpatterns = [
    path('', views.index,name="index"),
    path('admin_register/', views.admin_register, name="admin_register"),
    path('mod_register/', views.mod_register, name="mod_register"),
    path('user_register/', views.user_register, name="user_register"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('mod_login/', views.mod_login, name="mod_login"),
    path('user_login/', views.user_login, name="user_login"),
]


