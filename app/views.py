from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import InputForm, NewUserForm

# Create your views here.
def index(request):
    return render(request,"users/index.html")

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "users/register.html", context={"register_form":form})

def login(request):
    context ={}
    context['form']= InputForm()
    return render(request,"users/login.html",context)
