from django.shortcuts import render
from django.views.generic import *
from django.urls import *
from .forms import *

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'