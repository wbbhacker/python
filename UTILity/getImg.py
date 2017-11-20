#!/usr/bin/env python
#coding:utf-8
# python3
import os
import json
import sys

def getImgJson(path,flag=True):
	imgArray = []
	for root, dirs, files in os.walk(path, topdown=False):
		for file in files:
			imgPath = os.path.join(root, file)[len(path)+1:]
			fileImg = path.split('\\')[-1]
			pathStr = '\''+fileImg+'/'+imgPath.replace('\\','/')+'\''
			imgArray.append(pathStr)
	if flag == True:
		imgStr = '[\n' + ',\n'.join(imgArray) + '\n]'
	else:
		imgStr = '[' + ','.join(imgArray) + ']'

	with open('account.js','w',encoding='utf-8') as f:
		f.write(imgStr)
	print ('写入account.js成功......')

if __name__ == '__main__':
	if len(sys.argv) == 2 :
		getImgJson(sys.argv[1])
	elif len(sys.argv) == 1:
		print('请输入图片文件夹路径！')
	else:
		if sys.argv[2] == 'false':
			getImgJson(sys.argv[1],False)
		else:
			getImgJson(sys.argv[1],True)