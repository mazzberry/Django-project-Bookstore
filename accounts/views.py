from django.shortcuts import render, redirect

from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import CustomUser, CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

#Create your views here.

class SignUpView(generic.CreateView):
    
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = 'login'


    