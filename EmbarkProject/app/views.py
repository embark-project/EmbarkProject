from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import InputForm, Admin_Form, Mod_Form, User_Form
from .models import User_type
from . import forms
from . import models

choices = [0,1,2]
# Create your views here.
def index(request):
    return render(request,"users/index.html")

def admin_register(request):
    form = Admin_Form(request.POST)
    if request.method == 'POST':
        username  = request.POST.get('username', '')
        email     = request.POST.get('email', '')
        password = request.POST.get('password1', '')
        password2 = request.POST.get('password2','')
        role = 0
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists.")
        if password == password2 and not User.objects.filter(username=username).exists():
            obj = User.objects.create_user(username=username, email=email, password=password)
            obj.save()
        return render(request, 'users/register.html', {'Admin_Form':form, "choices":choices})

    return render(request, 'users/register.html', {'Admin_Form':form, "choices":choices})

def mod_register(request): 
    form = Mod_Form(request.POST)
    if request.method == 'POST':
        username     = request.POST.get('username', '')
        email     = request.POST.get('email', '')
        password = request.POST.get('password1', '')
        password2 = request.POST.get('password2','')
        role = 1
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists.")
        if password == password2 and not User.objects.filter(username=username).exists():
            obj = User_type.objects.create(username=username, email=email, password=password, role='moderator')
            obj.save()
            return render(request, 'users/register.html', {'Mod_Form':form, "choices":choices})

    return render(request, 'users/register.html', {'Mod_Form':form, "choices":choices})
        
def user_register(request):
    form = User_Form(request.POST)
    if request.method == 'POST':
        username     = request.POST.get('username', '')
        email     = request.POST.get('email', '')
        password = request.POST.get('password1', '')
        password2 = request.POST.get('password2','')
        address = request.POST.get('address','')
        phone = request.POST.get('phone','')
        role = 2
        if User_type.objects.filter(username=username).exists():
            messages.error(request,"Username already exists.")
        if password == password2 and not User.objects.filter(username=username).exists():
            obj = User_type.objects.create(username=username, email=email, password=password, 
                address=address, phone=phone, role='user')
            obj.save()
            return render(request, 'users/register.html', {'User_Form':form, "choices":choices})

    return render(request, 'users/register.html', {'User_Form':form, "choices":choices})

def mod_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = 'moderator'
        if not User_type.objects.filter(username=username, password=password, role='moderator').exists():
            return redirect('mod_home')
            #messages.error(request, "Invalid")
        else:
            messages.error(request, "Invalid")
    form = InputForm(request.POST)
    context ={}
    context['form']= InputForm()
    return render(request,"users/login.html", context)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = 'user'
        if not User_type.objects.filter(username=username, password=password, role='user').exists():
            return redirect('user_home')
            #messages.error(request, "Invalid")
        else:
            messages.error(request, "Invalid")
    form = InputForm(request.POST)
    context ={}
    context['form']= InputForm()
    return render(request,"users/login.html", context)

def mod_logout(request):
    return redirect('mod_login')

def user_logout(request):
    return redirect('user_login')

def mod_home(request):
    return render(request,"users/moderators/mod_home.html")

def user_home(request):
    return render(request,"users/endusers/user_home.html")

def profile_view(request):
    doc = User_type.objects.all()
    d = {'doc': doc} 
    return render(request,'users/profile.html', d)


def delete_profile(request,pid):
    doc_del = User_type.objects.get(id=pid)
    doc_del.delete()
    return redirect('profile_view')


 