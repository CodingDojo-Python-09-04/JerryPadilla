# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.


def index(request):
    if request.session.get('counter') == None:
        request.session['counter'] = 0
    request.session['counter'] += 1
    return render(request, 'generator/index.html')

def reset(request):
    try:
        del request.session['counter']
    except KeyError:
        pass
    return redirect('/')

def random_word(request):
    request.session.pop('random_word')
    request.session['random_word'] = get_random_string(length=14)
    return redirect('/')
