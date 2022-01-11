from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import fields, models
from .models import User_type
from django.contrib.auth.forms import UserChangeForm

User = get_user_model()
# Create your forms here.

class Admin_Form(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User_type
        fields = ("username", "email", "password1", "password2")

class Mod_Form(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = User_type
        fields = ("username", "email", "password1", "password2","address")
 

class User_Form(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = User_type
        fields = ("username", "email", "password1", "password2","address", "phone")

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User_type
        fields = ['phone']
