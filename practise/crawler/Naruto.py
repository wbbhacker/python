#!/usr/bin/env python
#coding:utf-8
import os
import sys  
import re
import urllib2
import decodeM
from bs4 import BeautifulSoup
reload(sys)  
sys.setdefaultencoding('utf8')  

class naruto:

	def __init__(self,url):

		soup = self.getHtml(url,True)
		chapters = soup.find_all('ol', class_='chapter-page-all')[0].find_all('span',class_='works-chapter-item')

		index = 1

		for i in chapters :
			try:
				file_path = 'img/'+i.a['title']
				# os.mkdir(file_path)
				htmlStr = self.getHtml('http://ac.qq.com'+i.a['href'])

				if index == 1 :				
					index = 2
					data = re.search(r'\'\S{200,}\'',htmlStr).group()
					print type(data)
					with open('demo.txt','wb') as fp:
						fp.write(data)
					print decodeM.decode(data) 

			except Exception,e:
				print '**************************************'
				print Exception,':',e

	def getHtml(self,url,flag=False):

		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		html = response.read()
		if flag == True:
			html = BeautifulSoup(html)
		return html


	@staticmethod
	def download(url,save_path):

		imgData = urllib2.urlopen(url).read()

		with open(save_path,'wb') as fp:
			fp.write(imgData)


if __name__ == '__main__':

	# url = 'http://ac.tc.qq.com/store_file_download?buid=15017&uin=1468625909&dir_path=/&name=16_07_38_51ce7aa442438201fa8d052de6fcfaf4_3193.jpg'
	# save_path = 'img/2.jpg'

	demo = naruto('http://ac.qq.com/Comic/comicInfo/id/544907')
	# demo = naruto('http://ac.qq.com/ComicView/index/id/544907/cid/24')



