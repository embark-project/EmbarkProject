from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
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
        username     = request.POST.get('username', '')
        email     = request.POST.get('email', '')
        password = request.POST.get('password1', '')
        password2 = request.POST.get('password2','')
        role = 0
        if password == password2:
            obj = User_type(username=username, email=email, password=password, role='admin')
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
        address = request.POST.get('address','')
        role = 1
        if password == password2:
            obj = User_type(username=username, email=email, password=password,
                address=address, role='moderator')
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
        dob = request.POST.get('dob','')
        phone = request.POST.get('phone','')
        role = 2
        if password == password2:
            obj = User_type(username=username, email=email, password=password, 
                address=address, dob=dob, phone=phone, role='user')
            obj.save()
            return render(request, 'users/register.html', {'User_Form':form, "choices":choices})

    return render(request, 'users/register.html', {'User_Form':form, "choices":choices})

'''
def admin_register(request):
    form = Admin_Form(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        form.username = form.cleaned_data['username']
        form.email = form.cleaned_data['email']
        form.password = form.cleaned_data['password']
        form = Admin_Form()
        login(request, user)
        messages.success(request, "Registration successful." )
        return redirect("index.html")
    messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, "users/register.html", context={"Admin_Form":form, "choices":choices})


def mod_register(request):
    if request.method == "POST":
        form = Mod_Form(request.POST)
        user = User_type(username=username, email=email, password=password, address=address)
        if form.is_valid():
            form = User_type()
            form.username = form.cleaned_data['username']
            form.email = form.cleaned_data['email']
            form.password = form.cleaned_data['password']
            form.address = form.cleaned_data['address']
            user = form.save()

            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = Mod_Form()
    return render(request, "users/register.html", context={"Mod_Form":form, "choices":choices})

def user_register(request):
    if request.method == "POST":
        form = User_Form(request.POST)
        if form.is_valid():
            form = User_type()
            form.username = form.cleaned_data['username']
            form.email = form.cleaned_data['email']
            form.password = form.cleaned_data['password']
            form.address = form.cleaned_data['address']
            form.dob = form.cleaned_data['dob']
            form.phone = form.cleaned_data['phone']
            user = form.save()
            
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = User_Form()
    return render(request, "users/register.html", context={"User_Form":form, "choices":choices})
'''
def admin_login(request):
    context ={}
    context['form']= InputForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User_type(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("templates/moderators/mod_home.html")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"users/login.html",context)

def mod_login(request):
    context ={}
    context['form']= InputForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("templates/moderators/mod_home.html")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"users/login.html",context)

def user_login(request):
    context ={}
    context['form']= InputForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"users/login.html",context)
'''
def login(request):
    context ={}
    context['form']= InputForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"users/login.html",context)
    '''