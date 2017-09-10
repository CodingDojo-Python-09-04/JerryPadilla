# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Users Page')

def register(request):
    return HttpResponse('Registering new user')

def login(request):
    return HttpResponse('Logging in new user')

def users(request):
    return HttpResponse('List of Current Users')
