#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 00:22:59 2019

@author: sekikazuma
"""
#from django.contrib import admin
from django.urls import path
from . import views
from django.urls import re_path
#from django.contrib.auth.views import logout

urlpatterns = [
     #path('',views.top,name='top'),
     #path('up_load',views.up_load,name='up_load'),
     path('view', views.view, name='view'),
     path('up_load', views.up_load.as_view(), name='up_load'),
     re_path(r'^article_update/(?P<pk>\d+)/$', views.ArticleUpdateView.as_view(), name="article_update"),
     path('article_list_view', views.ArticleListView.as_view(), name='article_list_view'),
     path('article_delete',views.DeleteView.as_view(),name = 'article_delete'),
     re_path(r'^article_detail_view/(?P<pk>\d+)/$',views.ArticleDetailView.as_view(),name = 'article_detail_view'),
     path('add', views.add, name='add'),
]
