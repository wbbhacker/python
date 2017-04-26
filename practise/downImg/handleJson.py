#!/usr/bin/env python
#coding:utf-8

import json

def loadJson():
	data = []
	obj = json.load(open('data.json'))['log']['entries']
	for i in obj:
		v = i['request']['headers'][5]['value']
		if v == 'image/webp,image/*,*/*;q=0.8':
			data.append(i['request']['url'])
	return data