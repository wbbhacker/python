#!/usr/bin/env python
#coding:utf-8
import os 
import re
import json
import urllib2
from bs4 import BeautifulSoup

class naruto:

    def __init__(self,url):

        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        html = response.read()

        print html


if __name__ == '__main__':

    demo = naruto('https://g.hz.netease.com/sale_test/go/tree/master')



