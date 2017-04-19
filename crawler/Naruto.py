#!/usr/bin/env python
#coding:utf-8
import os
# import logging
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# request = urllib2.Request('http://www.baidu.com')
# response = urllib2.urlopen(request)
# html = response.read()
# soup = BeautifulSoup(html)


class naruto:

	def __init__(self,url):

		browser = webdriver.PhantomJS('phantomjs')
		browser.get(url)
		elem = browser.find_element_by_id('comicContain').find_elements_by_css_selector('img')
		for i in elem :

			print i.get_attribute('src')


		# print  browser.find_element_by_id('comicTitle')



		# soup = self.getHtml(url)
		# span = soup.find_all('ol', class_='chapter-page-all')[0].find_all('span',class_='works-chapter-item')

		# index = 1
		# for i in span :
		# 	try:
		# 		file_path = 'img/'+i.a['title']
		# 		# os.mkdir(file_path)
		# 		soup = self.getHtml('http://ac.qq.com'+i.a['href'])

		# 		if index == 1 :				
		# 			index = 2
		# 			# print file_path
		# 			a = soup.find_all('ul',class_='comic-contain')[0]
		# 			b = soup.find_all('script')
		# 			print b

		# 	except Exception,e:
		# 		print '*************************************x *'
		# 		print Exception,':',e

	def getHtml(self,url):

		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		html = response.read()
		soup = BeautifulSoup(html)
		return soup

	@staticmethod
	def download(url,save_path):

		imgCon = urllib2.urlopen(url).read()
		with open(save_path,'wb') as fp:
			fp.write(imgCon)

		# print imgCon

if __name__ == '__main__':

	# url = 'http://ac.tc.qq.com/store_file_download?buid=15017&uin=1468625909&dir_path=/&name=16_07_38_51ce7aa442438201fa8d052de6fcfaf4_3193.jpg'
	# save_path = 'img/2.jpg'

	# demo = naruto('http://ac.qq.com/Comic/comicInfo/id/544907')
	demo = naruto('http://ac.qq.com/ComicView/index/id/544907/cid/24')
	

	# demo.download(url)



