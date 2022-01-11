from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_type, Req, Order 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import Admin_Form, Mod_Form, User_Form

#class Mod_Form(UserCreationForm):
#    class Meta:
#        model = User_type
#
#class User_Form(UserChangeForm):
#    class Meta:
#        model = User_type

class MyUserAdmin(UserAdmin):
    form = Mod_Form
    add_form = User_Form
    model = User_type
    list_display = ['username', 'email', 'address', 'phone','role']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('address', 'phone','role')}),
    ) #this will allow to change these fields in admin module


admin.site.register(User_type, MyUserAdmin) 
admin.site.register(Req) 
admin.site.register(Order) 

