#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name=input('Please input a name:')
#print('Your name is:', name)

#打印爱心
#print('\n'.join([''.join([('Love'[(x-y)%4]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

'''
import random
range1 = int(input("请设置本次猜数字游戏的最小值:"))
range2 = int(input("请设置本次猜数字游戏的最大值:"))
num = random.randint(range1,range2)
guess = 0
print("猜数字游戏开始！")
i = 0
while guess != num:
    i += 1
    guess = int(input("请输入你猜想的数字："))
 
    if guess == num:
        print("恭喜，你猜对了！")
    elif guess < num:
        print("你猜的数字小了...")
    else:
        print("你猜的数字大了...")
 
print("你总共猜了%d" %i + "次,快和小伙伴们分享一下吧")
'''

'''
#互不相同且不重复的三位数
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j)and(i!=k)and(j!=k):
                print (i,j,k)
'''


l=[]
for i in range(3):
    x = int(input("Please input an integer:\n"))
    l.append(x)
l.sort()
print (l)
