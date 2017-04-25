#!/usr/bin/env python
#coding:utf-8

import json

def loadJson():
	
	jsonData = open('data.json')
	obj = json.load(jsonData)
	return obj['log']['version']

if __name__ == '__main__':

	data= loadJson()

	print data