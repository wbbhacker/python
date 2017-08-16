#!/usr/bin/env python
#coding:utf-8

import xlrd
from collections import OrderedDict
import json
import codecs

# 解决中文乱码
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

wb = xlrd.open_workbook('s.xlsx')

convert_list = []


for idx in range(0,4):

	sh = wb.sheet_by_index(idx)
	title = sh.row_values(0)
	for rownum in range(1, sh.nrows):
	    rowvalue = sh.row_values(rownum)
	    single = OrderedDict()
	    for colnum in range(0, len(rowvalue)):

	        single[title[colnum]] = rowvalue[colnum]
	        single['城市'] = sh.name

	    convert_list.append(single)
    
j = json.dumps(convert_list,ensure_ascii=False)

with codecs.open('file.json',"w") as f:
    f.write(j)