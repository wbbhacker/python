# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	a = request.GET['a']
	b = request.GET.get('b',10)
	c = int(a) + int(b)
	return HttpResponse(c)


def detail(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))


def login(request):
	return render(request,'login.html')


def home(request):
	return render(request,'home.html')
