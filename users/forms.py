from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import TextInput
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age',)
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': "form-control"}),
            'age' : TextInput(attrs={'class':'form-control'}),
        }

class CustomerUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')

# class CustomUserLoginForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password',)
#         widgets = {
#             'username': TextInput(attrs={'class':'form-control'}),
#             'password': TextInput(attrs={'class': 'form-control'}),
#         }