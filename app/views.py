from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import InputForm, Admin_Form, Mod_Form, User_Form

choices = [0,1,2]
# Create your views here.
def index(request):
    return render(request,"users/index.html")

def admin_register(request):
    if request.method == "POST":
        form = Admin_Form(request.POST)
        a_id = 0 
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = Admin_Form()
    return render(request, "users/register.html", context={"Admin_Form":form, "a_id":0, "choices":choices})

def mod_register(request):
    if request.method == "POST":
        form = Mod_Form(request.POST)
        m_id = 1
        if form.is_valid():
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
        u_id=2
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = User_Form()
    return render(request, "users/register.html", context={"User_Form":form, "choices":choices})

def login(request):
    context ={}
    context['form']= InputForm()
    return render(request,"users/login.html",context)
