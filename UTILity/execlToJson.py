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

wb = xlrd.open_workbook('suteng.xls')

convert_list = []

sh = wb.sheet_by_index(0)
title = sh.row_values(0)

for rownum in range(1, sh.nrows):
    rowvalue = sh.row_values(rownum)
    single = OrderedDict()
    for colnum in range(0, len(rowvalue)):
        print(title[colnum], rowvalue[colnum])
        single[title[colnum]] = rowvalue[colnum]

    convert_list.append(single)
    
j = json.dumps(convert_list,ensure_ascii=False)

with codecs.open('file.json',"w") as f:
    f.write(j)