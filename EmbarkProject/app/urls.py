from django.contrib import admin
from django.urls import path, include
from app import views
from django.contrib.auth import views as auth_views
from .views import UserEditView, index, login
from .views import admin_register, mod_register, user_register, UserEditView

admin.autodiscover()

urlpatterns = [
    path('', views.index,name="index"),
    path('admin_register/', views.admin_register, name="admin_register"),
    path('mod_register/', views.mod_register, name="mod_register"),
    path('user_register/', views.user_register, name="user_register"),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name="logout"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('mod_home/', views.mod_home, name="mod_home"),
    path('user_home/', views.user_home, name="user_home"),
    path('profile_view/', views.profile_view, name="profile_view"),
    path('delete_profile(<int:pid>)/', views.delete_profile, name='delete_profile'),
    path('post_requirements', views.post_requirements, name="post_requirements"),
    path('view_requirements/', views.view_requirements, name="view_requirements"),
    path('add_order/', views.add_order, name="add_order"),
    path('edit_profile/',UserEditView.as_view(), name='edit_profile')
]




