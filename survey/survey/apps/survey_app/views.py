# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.



def index(request):

    return render(request, 'survey_app/index.html')

def process(request):
    # if request.method == 'POST':
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['dojo_location']
    request.session['language'] = request.POST['favorite_language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')

def result(request):
    if request.session.get('counter') == None:
        request.session['counter'] = 0
    request.session['counter'] += 1

    post_info = {
        'name':request.session['name'],
        'location':request.session['location'],
        'language':request.session['language'],
        'comment':request.session['comment']
    }
    return render(request, 'survey_app/result.html', post_info)
