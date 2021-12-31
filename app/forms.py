from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

YEARS= [x for x in range(1940,2021)]

# Create your forms here.

class Admin_Form(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

    def save(self, commit=True):
        user = super(Admin_Form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class Mod_Form(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2","address")

    def save(self, commit=True):
        user = super(Mod_Form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user

class User_Form(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    DOB = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2","address","DOB", "phone")

    def save(self, commit=True):
        user = super(User_Form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']
        user.DOB = self.cleaned_data['DOB']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user

class InputForm(forms.Form):

    user_name = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput())
