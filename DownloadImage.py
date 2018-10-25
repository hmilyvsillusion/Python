#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author Kevin Kong

import re
import os
import requests


def mkdir(foldername):
    #获取当前文件夹路径~~
    path = os.getcwd()
    folder = os.path.exists(path+'/'+foldername+"/")

    if not folder:
        os.makedirs(path+"/"+foldername+"/")
        print("您的搜索结果将放在文件夹"+path+"/"+foldername+"/中")
    else:
        print("您的搜索结果将放在文件夹"+path+"/"+foldername+"/中")


def nextSource(content): # 通过正则获取下一页的网址
          next = re.findall('<div id="page">.*<a href="(.*?)" class="n">',content,re.S)[0]
          #print("---------" + "http://image.baidu.com" + next) 
          return "http://image.baidu.com" + next


def downloadPic(html, keyword,num,filename):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    print('找到关键词 -[' + keyword + ']- 的图片，现在开始下载图片...\n')
    print("Downloading Images...Please wait...")
    i = 1
    #判断是否已经输出过第一页的内容
    flag=0   
    while True:
        
        if(flag==0):
            for each in pic_url:
             print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
             try:
                pic = requests.get(each, timeout=10)
             except requests.exceptions.ConnectionError:
              print('无法下载该图片，超时')
              continue
             
             #'../'+
             dir = filename+'/' + keyword + '_' + str(i) + '.jpg'
             fp = open(dir, 'wb')
             fp.write(pic.content)
             fp.close()
             i += 1
             flag=1
             if i>num:
                break
        
        #首先需要获取下一页搜索结果的地址
        else:
            for index in range(0,3):
                next_url = nextSource(html)#下一个页面的URL
                #print(next_url)#采集页面图片地址信息
                #下一个页面的信息
                next_content = requests.get(next_url)

                
            #将下一个页面的内容赋值到HTML上
            #if(html==next_content.text):
               # print("Same")
           # else:
              #  print("Different")
                html=next_content.text
                index +=1
            
            #下一个页面图片的URL
                #由于百度图片页面的特殊性，一个网页上有60张图片，但是只显示20张，所以爬完第一页就直接跳到第四页开始爬，仅仅是针对百度图片
            next_pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
            for next_each in next_pic_url:
                print('正在下载第' + str(i) + '张图片，图片地址:' + str(next_each))
                try:
                    next_pic = requests.get(next_each, timeout=10)
                except requests.exceptions.ConnectionError:
                    print('无法下载该图片，超时')
                    continue

                #'../'+
                dir = filename+'/' + keyword + '_' + str(i) + '.jpg'
                fp = open(dir, 'wb')
                fp.write(next_pic.content)
                fp.close()
                i += 1
                #如果不加if判断，整个for循环就会全部执行，起不到数量上的限定作用           
                if i>num:
                    break
               
        if i>num:
            break
    
    path=os.getcwd()
    print("\n本次下载共下载了"+str(i-1)+"张图片！\n")
    print("图片存放于"+path+"/"+filename+"文件夹中。\n")
    input("按回车键退出程序...")    

if __name__ == '__main__':
    print("\n")
    print("This is a programe to search and download images automatically.")
    word = input("Input a key word to search and download images:  ")
    #由于输入的信息属于字符串，需要进行数据类型转换
    limit = int(input("How many images you want to downlaod, please input a number: "))
    filename=input("Creating a folder for your images, please name your folder：")
    #根据输入的文件夹名调用mkdir函数来创建文件夹
    mkdir(filename)
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    result = requests.get(url)
    #调用downloadPic函数搜索并下载图片
    downloadPic(result.text, word,limit,filename)