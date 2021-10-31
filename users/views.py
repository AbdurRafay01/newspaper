from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import CustomerUserChangeForm, CustomUserForm
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

# class LoginView(FormView):
#     form_class = CustomUserLoginForm
#     success_url = reverse_lazy('article_list')
#     template_name = 'registration/login.html'