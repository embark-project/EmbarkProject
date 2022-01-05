from django.contrib import admin
from django.urls import path, include
from app import views
from .views import index, login
from .views import admin_register, mod_register, user_register, profile_view, delete_profile

admin.autodiscover()

urlpatterns = [
    path('', views.index,name="index"),
    path('admin_register/', views.admin_register, name="admin_register"),
    path('mod_register/', views.mod_register, name="mod_register"),
    path('user_register/', views.user_register, name="user_register"),
    #path('admin', views.admin, name="admin"),
    path('mod_login/', views.mod_login, name="mod_login"),
    path('user_login/', views.user_login, name="user_login"),
    path('logout/',views.mod_logout, name="logout"),
    path('logout/',views.user_logout, name="logout"),
    path('mod_home/', views.mod_home, name="mod_home"),
    path('user_home/', views.user_home, name="user_home"),
    path('profile_view/', views.profile_view, name="profile_view"),
    path('delete_profile(?P<int:pid>)/', delete_profile, name='delete_profile'),
]


