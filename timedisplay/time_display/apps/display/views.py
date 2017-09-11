# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from datetime import datetime
from time import gmtime, strftime
# Create your views here.


def index(request):
    context = {
        'time':strftime("%Y-%m-%d %H:%M %p", gmtime()),
        'time2':datetime.now()
    }
    return render(request, 'display/index.html', context)


# strftime("%Y-%m-%d %H:%M %p", gmtime())
