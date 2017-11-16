#!/usr/bin/env python
#coding:utf-8

# python3

import os
import re
import time 

timer = int(time.time())

print('版本号为:'+str(timer))

def findfile(url):
	reg = r'\.(css|js|html)'

	for root, dirs, files in os.walk(url, topdown=False):
		for file in files:
			if re.search(reg,file) != None:
				# print(os.path.join(root, file))
				addRev(os.path.join(root, file))

def replace(m):

	# reg = r'\.(png|jpg|gif|js|css)(\"|\'){1}'
	reg = r'\.(png|jpg|gif|js|css)'

	# print(re.search(r'(\'|\")',m.group()).group())

	return re.search(reg,m.group()).group()+ '?v=' + str(timer) + re.search(r'(\'|\")',m.group()).group()

def addRev(url):

	reg = r'\.(png|jpg|gif|js|css)(\?v=[0-9]*)*(\"|\'){1}'

	atext = ''

	with open(url,'r',encoding='utf-8') as f:

		atext = re.sub(reg,replace,f.read())

	with open(url,'w',encoding='utf-8') as f:
		f.write(atext)
		print ('写入成功......')

if __name__ == '__main__':
	path = '/Users/binbinwang/workspace/local/src'
	findfile(path)

