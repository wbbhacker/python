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

	paths = os.path.split(path);

	if os.path.exists(paths[0]) == False:
		os.makedirs(paths[0])

	imgCon = urllib2.urlopen(url).read()

	with open(path,'wb') as fp:
		fp.write(imgCon)

if __name__ == '__main__':

	loadImg()