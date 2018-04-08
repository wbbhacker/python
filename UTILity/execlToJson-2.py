#!/usr/bin/env python
#coding:utf-8

import xlrd
from collections import OrderedDict
import json
import codecs


wb = xlrd.open_workbook('data.xlsm')

convert_list = []

sh = wb.sheet_by_index(0)
title = sh.row_values(0)


print(title)

for rownum in range(1,sh.nrows):
	rowValue = sh.row_values(rownum)
	single = OrderedDict()
	for colnum in range(0, len(rowValue)):
	        single[title[colnum]] = rowValue[colnum]

	convert_list.append(single)
j = json.dumps(convert_list,ensure_ascii=False,separators=(',\n', ':'))

with codecs.open('file.json','w','utf-8') as f:
    f.write(j)