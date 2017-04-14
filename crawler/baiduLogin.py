#!/usr/bin/env python
#coding:utf-8

import urllib2
from bs4 import BeautifulSoup


request = urllib2.Request('http://www.baidu.com')

response = urllib2.urlopen(request)

html = response.read()

soup = BeautifulSoup(html)


print soup.select('a')