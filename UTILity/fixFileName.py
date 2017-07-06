#!/usr/bin/env python
#coding:utf-8

import os

def fixFileName(path):
	
	for root, dirs, files in os.walk(path):
		for i in files:
			ext = i.split('.')[-1]
			if ext != 'css' and ext != 'html' and ext != 'gif' :
				# print '******************************************************'
				orgName = path + '/' + i
				newName = path + '/'.join(i.split('.')[0:-1])
				# print 'newName:' + newName
				# print orgName
				os.rename(orgName,newName)

if __name__ == '__main__':
	fixFileName('resource')