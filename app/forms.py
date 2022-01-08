from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User_type

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
