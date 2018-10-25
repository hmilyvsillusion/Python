#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#权限检查
userbase=[
    ['albert','1234'],
    ['bill','2234'],
    ['william','3234'],
    ['bob','4234']
]
username=input('Please enter your username:')
password=input('Enter your password:')
if [username,password] in userbase:
    print('Access Granted')
else:
    print('Access Denied')




    