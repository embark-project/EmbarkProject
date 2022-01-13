from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Admin_Form, Mod_Form, User_Form, EditProfileForm
from .models import User_type, Req, Order 
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login 
from django.urls import reverse_lazy
from django.urls import reverse


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
        if User_type.objects.filter(username=username).exists():
            messages.error(request,"Username already exists.")
        if password == password2 and not User_type.objects.filter(username=username).exists():
            obj = User_type.objects.create_user(username=username, email=email, password=password,
             role='admin',is_staff='True',is_superuser='True')
            user = obj.save()
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
                return redirect('admin_home')
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
    auth_logout(request)
    return redirect('login')

def admin_home(request):
    return render(request,"users/admin/admin_home.html")

def mod_home(request):
    return render(request,"users/moderators/mod_home.html")

def user_home(request):
    return render(request,"users/endusers/user_home.html")

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')
 
@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile_view')
    form = EditProfileForm(instance=request.user)
    args = {'form':form}
    return render(request,"users/edit_profile.html",args)


@login_required
def post_requirements(request):
    if request.method == 'POST':
        cat = request.POST['category']
        prod = request.POST['product']
        obj = Req(category=cat, product=prod)
        obj.save()
        messages.info(request,"Requirements needed")
             
    return render(request, 'users/admin/post_requirements.html')

@login_required
def view_requirements(request):
    d = {'order': Order.objects.all()}
    messages.info(request,"User posted a new requirement. Waiting for your approval")
    return render(request, 'users/moderators/view_requirements.html',d)

@login_required
def approve(request):
    pass

@login_required
def decline(request):
    pass

@login_required
def approved(request,order_id):
    t = Order.objects.get(order_id=order_id)
    t.approved_status = 1
    t.save() 
    messages.info(request,"Request approved")
    return HttpResponseRedirect(reverse('view_requirements'))

@login_required
def declined(request,order_id):
    t = Order.objects.get(order_id=order_id)
    t.approved_status = 2
    t.save()
    messages.info(request,"Request Declined")
    return HttpResponseRedirect(reverse('view_requirements'))

@login_required
def approval_requirements(request):
    d = {'order': Order.objects.filter(approved_status=1)}
    order_ids = request.POST.getlist("order_id")
    price = request.POST.getlist("price")
    pending = {'order': Order.objects.filter(price=0, approved_status=1)}
    for i in range(len(order_ids)):
        Order.objects.filter(order_id=order_ids[i]).update(price=price[i])
    
    return render(request, 'users/admin/approval_requirements.html',pending)

@login_required
def add_order(request):
    if request.method == 'POST':
        cat = request.POST['order_cat']
        prod = request.POST['order_prod']
        obj = Order(category=cat, product=prod)
        obj.save()
        messages.success(request,"New things are posted. Check it out")
    d = {'order': Req.objects.all()}

    return render(request, 'users/endusers/order.html',d)

 
@login_required
def view_offer(request):
    return render(request, 'users/endusers/offer.html')
