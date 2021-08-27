# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:09:59 2021

@author: PURUBOI
"""
a=[1,5,6,7,9]
b=[9,7,6,5,1]
l=[]
if len(a)==len(b):
    j=-1
    for i in range(0,len(a)):
        l.append(a[i]*b[j+len(b)])
        j-=1
    print(l)
else:
    print(-1)
            
            