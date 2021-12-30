from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import InputForm, Admin_Form, Mod_Form, User_Form

# Create your views here.
def index(request):
    return render(request,"users/index.html")

def admin_register(request):
    if request.method == "POST":
        form = Admin_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = Admin_Form()
    return render(request, "users/admin_register.html", context={"Admin_Form":form})

def mod_register(request):
    if request.method == "POST":
        form = Mod_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = Mod_Form()
    return render(request, "users/mod_register.html", context={"Mod_Form":form})

def user_register(request):
    if request.method == "POST":
        form = User_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = User_Form()
    return render(request, "users/user_register.html", context={"User_Form":form})

def login(request):
    context ={}
    context['form']= InputForm()
    return render(request,"users/login.html",context)
