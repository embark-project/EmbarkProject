from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User_type

User = get_user_model()
# Create your forms here.

class Admin_Form(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User_type
        fields = ("username", "email", "password1", "password2")

        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

class Mod_Form(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = User_type
        fields = ("username", "email", "password1", "password2","address")

        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

class User_Form(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = User_type
        fields = ("username", "email", "password1", "password2","address", "phone")

        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User_type
        fields = ("username", "email", "phone","address")

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
        }
        help_texts = {
            'username': None, 
            }
         


