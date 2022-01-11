from django.contrib import admin
from django.urls import path, include
from app import views
from django.contrib.auth import views as auth_views
from .views import index, login
from .views import admin_register, mod_register, user_register, add_order

admin.autodiscover()

urlpatterns = [
    path('', views.index,name="index"),
    path('admin_register/', views.admin_register, name="admin_register"),
    path('mod_register/', views.mod_register, name="mod_register"),
    path('user_register/', views.user_register, name="user_register"),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name="logout"),
    path('mod_home/', views.mod_home, name="mod_home"),
    path('user_home/', views.user_home, name="user_home"),
    path('profile/', views.profile, name="profile"),
    path('delete_profile(<int:pid>)/', views.delete_profile, name='delete_profile'),
    path('requirements_view/', views.requirements_view, name="requirements_view"),
    path('add_order/', views.add_order, name="add_order")
]



