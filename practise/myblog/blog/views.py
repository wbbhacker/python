# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Article

from datetime import datetime
# Create your views here.

def index(request):
	return HttpResponse('hello,world,Django')


def detail(request,my_args):
	post = Article.objects.all()[int(my_args)]
	str = ('title = %s,category = %s, data_time = %s,content = %s' % (post.title,post.category,post.data_time,post.content))
	return HttpResponse(str)
def home(request):
	post_list = Article.objects.all()
	return render(request,'home.html',{'post_list':post_list})


#测试————————————————————————————
def test(request):
	return render(request,'test.html',{'current_time':datetime.now()})
def base(request):
	return render(request,'base.html')





