#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 00:40:52 2019

@author: sekikazuma
"""

from django import forms
from .models import Document
#from .models import CustomUser
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        #fields = ('user','description', 'photo', )
        fields = ('author','title','description', 'photo', )
