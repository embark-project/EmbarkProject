from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import Admin_Form, Mod_Form, User_Form
from .models import User_type 
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login


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
        if password == password2 and not User_type.objects.filter(username=username).exists():
            obj = User.objects.create_user(username=username, email=email, password=password,
             role='admin')
            user = obj.save()
            login(request, user)
        return render(request, 'users/register.html', {'Admin_Form':form, "choices":choices})

    return render(request, 'users/register.html', {'Admin_Form':form, "choices":choices})

def mod_register(request): 
    form = Mod_Form(request.POST)
    if request.method == 'POST':
        username     = request.POST.get('username', '')
        email     = request.POST.get('email', '')
        password = request.POST.get('password1', '')
        password2 = request.POST.get('password2','')
        address = request.POST.get('address','')
        role = 1
        if User_type.objects.filter(username=username).exists():
            messages.error(request,"Username already exists.")
        if password == password2 and not User_type.objects.filter(username=username).exists():
            obj = User_type.objects.create_user(username=username, email=email, password=password, 
                address=address, role='moderator',is_staff='True')
            user = obj.save()
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
        if password == password2 and not User_type.objects.filter(username=username).exists():
            obj = User_type.objects.create_user(username=username, email=email, password=password, 
                address=address, phone=phone, role='user')
            user = obj.save()
            login(request, user)
            return render(request, 'users/register.html', {'User_Form':form, "choices":choices})

    return render(request, 'users/register.html', {'User_Form':form, "choices":choices})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff and user.is_active and user.is_superuser:
                auth_login(request, user)
                return redirect('index')
            elif user is not None and user.is_staff and user.is_active :
                auth_login(request, user)
                return redirect('mod_home')
            elif user is not None and user.is_active:
                auth_login(request, user)
                return redirect('user_home')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    else:
            msg = 'error validating form'
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form, 'msg': msg})

def logout(request):
    return redirect('login')

def mod_home(request):
    return render(request,"users/moderators/mod_home.html")

def user_home(request):
    return render(request,"users/endusers/user_home.html")

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


def delete_profile(request,pid):
    doc_del = User_type.objects.get(id=pid)
    doc_del.delete()
    return redirect('profile_view')

def requirements_view(request):
    return render(request, 'users/endusers/requirements.html')