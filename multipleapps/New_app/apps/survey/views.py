# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse('Hey survey time bro')

def new(request):
    return HttpResponse('Adding new user to servey shit')
