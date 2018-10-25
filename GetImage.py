#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import re
 
 
link = urllib.request.urlopen("http://dzh.mop.com/")
html_doc = link.read().decode("utf8")
jpg_list = re.findall('http.+?.jpg', html_doc)
n = 1
while n < len(jpg_list) + 1:
    urllib.request.urlretrieve(jpg_list[n - 1], str(n) + '.jpg')
    print("获取第" + str(n) + "张图片，网址是" + jpg_list[n - 1])
    n = n + 1
