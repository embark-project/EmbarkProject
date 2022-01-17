from django.contrib import admin
from django.urls import path, include
from app import views
from django.contrib.auth import views as auth_views
from .views import index, login
from .views import admin_register, mod_register, user_register, edit_profile

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
    path('edit_profile/',views.edit_profile, name='edit_profile'), 
    path('post_requirements', views.post_requirements, name="post_requirements"),
    path('history', views.history, name="history"),
    path('view_requirements/', views.view_requirements, name="view_requirements"), 
    path('approval_requirements/', views.approval_requirements, name="approval_requirements"),
    path('approve/', views.approve, name="approve"),
    path('decline/', views.decline, name="decline"),
    path('approved/<str:order_id>', views.approved, name="approved"),
    path('declined/<str:order_id>', views.declined, name="declined"),
    path('add_order/', views.add_order, name="add_order"),
    path('view_offer/', views.view_offer, name="view_offer"),
]




