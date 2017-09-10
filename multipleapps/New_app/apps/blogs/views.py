# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'Home page'
    return HttpResponse(response)

def blogs(request):
    response = 'placeholder to later display all the list of blogs'
    return HttpResponse(response)

def new(request):
    response = 'NEW BLOG'
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, number):
    response = 'Blog number {}'.format(number)
    return HttpResponse(response)

def edit(request, number):
    response = 'Edit blog number {}'.format(number)
    return HttpResponse(response)

def delete(request, number):
    response = 'delete blog number {}'.format(number)
    return HttpResponse(response)
