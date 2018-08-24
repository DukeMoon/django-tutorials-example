# -*- coding: utf-8 -*-
"""
@Time    : 2018-08-24 18:45
@Author  : DukeMoon
"""
from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name='index'),
]
