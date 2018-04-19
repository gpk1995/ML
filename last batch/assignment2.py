# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:29:14 2018

@author: user
"""

l=1
u=500
for n in range(l,u+1):
    order = len(str(n))
    s=0
    temp=n
    while temp>0 :
        num=temp%10
        s += num ** order
        temp = 10
if(n == s):
        print(n)