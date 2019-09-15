from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm # 追加

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm #ここを変更
    #form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
