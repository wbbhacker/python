# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Article(models.Model):
	
	title = models.CharField(max_length=100) #博客题目
	category = models.CharField(max_length=50,blank=True) #博客标签
	add_time = models.DateTimeField('保存日期',default=timezone.now) #博客日期
	mod_time = models.DateTimeField('最后修改日期',auto_now=True)

	content = models.TextField(blank=True,null=True) #博客文章正文

	def __unicode__(self):
		return self.title
	class Meta: #按时间下降排序
		ordering = ['-add_time']
	

