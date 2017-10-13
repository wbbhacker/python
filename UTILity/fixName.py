#!/usr/bin/env python
#coding:utf-8

import os

def fixName(path,name):

	for root, dirs, files in os.walk(path):
		
		for i in range(len(	files)):
			ext = files[i].split('.')[-1]

			orgName = path + '/' + files[i]
			newName = path + '/'+name+str(i)+'.'+ext
			os.rename(orgName,newName)

if __name__ == '__main__':
	fixName('kv-wen','kv-wen')                                                                                                                                                                                                                                                              