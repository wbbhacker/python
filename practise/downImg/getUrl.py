#!/usr/bin/env python
#coding:utf-8

import os
import re
import urllib2
from handleJson import loadJson

def loadImg():
	data = loadJson();
	for i in data:
		saveImg(i,i[31:])
		

def saveImg(url,path):
	imgCon = urllib2.urlopen(url).read()

	with open(path,'wb') as fp:
		fp.write(imgCon)

if __name__ == '__main__':

	loadImg()